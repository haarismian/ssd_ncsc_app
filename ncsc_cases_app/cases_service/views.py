from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.utils import timezone
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.http import require_POST
import logging

from .models import Case

# Create a logger for this module
logger = logging.getLogger(__name__)


class CaseListView(generic.ListView):
    model = Case
    template_name = 'cases_service/case_list.html'
    context_object_name = 'cases'

    def get_queryset(self):
        try:
            return Case.objects.all()
        except Exception as e:
            logger.exception("Error getting queryset in CaseListView: %s", e)
            return None


class CaseDetailView(generic.DetailView):
    model = Case
    template_name = 'cases_service/case_detail.html'
    context_object_name = 'case'

    def get_object(self, queryset=None):
        try:
            return super().get_object(queryset)
        except Http404 as e:
            logger.error("Case not found in CaseDetailView: %s", e)
            raise e
        except Exception as e:
            logger.exception("Error in CaseDetailView: %s", e)
            raise e


class CaseCreateView(LoginRequiredMixin, CreateView):
    model = Case
    fields = ['title', 'description']
    template_name = 'cases_service/create_case.html'
    success_url = reverse_lazy('cases_service:case_list')

    def form_valid(self, form):
        try:
            form.instance.user = self.request.user
            return super().form_valid(form)
        except Exception as e:
            logger.exception(
                "Error in form validation in CaseCreateView: %s", e)
            return self.form_invalid(form)


@require_POST
def delete_case(request, id):
    try:
        case = Case.objects.get(id=id)
        case.delete()
        return redirect('cases_service:case_list')
    except Case.DoesNotExist as e:
        logger.error("Case to delete not found: %s", e)
        raise Http404("Case does not exist")
    except Exception as e:
        logger.exception("Error deleting case: %s", e)
        return HttpResponse(status=500)
