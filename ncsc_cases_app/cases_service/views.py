from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.utils import timezone
from django.views.generic.edit import CreateView


from django.views.decorators.http import require_POST

from .models import Case


class CaseListView(generic.ListView):
    model = Case
    template_name = 'cases_service/case_list.html'
    context_object_name = 'cases'

    def get_queryset(self):

        return Case.objects.all()


class CaseDetailView(generic.DetailView):
    model = Case
    # Specify the template for case detail
    template_name = 'cases_service/case_detail.html'
    context_object_name = 'case'  # Name to access the case object in the template


class CaseCreateView(CreateView):
    model = Case
    fields = ['title', 'description']
    template_name = 'cases_service/create_case.html'
    success_url = reverse_lazy('cases_service:case_list')


# class DetailView(generic.DetailView):
#     model = Question
#     template_name = "cases_service/detail.html"

#     def get_queryset(self):
#         """
#         Excludes any questions that aren't published yet.
#         """
#         return Question.objects.filter(pub_date__lte=timezone.now())


@require_POST
def delete_case(request, id):
    case = Case.objects.get(id=id)
    case.delete()
    return redirect('cases_service:case_list')  # name of your case list URL
