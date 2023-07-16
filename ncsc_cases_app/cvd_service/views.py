from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django import forms


from django.urls import reverse_lazy
from django.views import generic
from .models import CvdReport
from django.utils import timezone
import logging

logger = logging.getLogger(__name__)

# Create your views here.


class CVDListView(LoginRequiredMixin, generic.ListView):
    model = CvdReport
    template_name = 'cvd_service/cvd_list.html'
    context_object_name = 'cvd_list'

    def get_queryset(self):
        # Return all CvdReport objects
        try:
            return CvdReport.objects.all()
        except Exception as e:
            logger.error('Error in CVDListView.get_queryset: %s', e)
            raise


class CVDDetailView(LoginRequiredMixin, generic.DetailView):
    model = CvdReport
    template_name = 'cvd_service/cvd_detail.html'


class CvdReportForm(forms.ModelForm):
    class Meta:
        model = CvdReport
        fields = ['first_name', 'last_name', 'email', 'phone', 'vulnerability_type',
                  'explanation', 'vulnerability_reason', 'domain_or_ip', 'pgp_key']

    def __init__(self, *args, **kwargs):
        super(CvdReportForm, self).__init__(*args, **kwargs)

        input_class = 'appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:ring-2 focus:ring-indigo-500'
        textarea_class = 'appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:ring-2 focus:ring-indigo-500'

        self.fields['first_name'].widget.attrs.update({'class': input_class})
        self.fields['last_name'].widget.attrs.update({'class': input_class})
        self.fields['email'].widget.attrs.update({'class': input_class})
        self.fields['phone'].widget.attrs.update({'class': input_class})
        self.fields['vulnerability_type'].widget.attrs.update(
            {'class': input_class})
        self.fields['explanation'].widget.attrs.update(
            {'class': textarea_class})
        self.fields['vulnerability_reason'].widget.attrs.update(
            {'class': textarea_class})
        self.fields['domain_or_ip'].widget.attrs.update(
            {'class': textarea_class})
        self.fields['pgp_key'].widget.attrs.update({'class': textarea_class})


class CVDCreateView(generic.CreateView):
    model = CvdReport
    form_class = CvdReportForm
    template_name = 'cvd_service/create_cvd.html'
    success_url = reverse_lazy('cvd_service:create_cvd')


@require_POST
def delete_cvd(request, pk):
    try:
        cvd = get_object_or_404(CvdReport, pk=pk)
        cvd.delete()
        # Redirect the user to the CVD list view after deleting
        return redirect('cvd_service:cvd_list')
    except Exception as e:
        logger.error('Error in delete_cvd: %s', e)
        raise
