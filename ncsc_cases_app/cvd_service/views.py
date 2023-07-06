from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


from django.urls import reverse_lazy
from django.views import generic
from .models import CvdReport
from django.utils import timezone

# Create your views here.


class CVDListView(LoginRequiredMixin, generic.ListView):
    model = CvdReport
    template_name = 'cvd_service/cvd_list.html'
    context_object_name = 'cvd_list'

    def get_queryset(self):
        # Creating dummy data
        CvdReport.objects.create(officer='Officer1',
                                 vulnerability_type='injection',
                                 explanation='Dummy explanation',
                                 vulnerability_reason='Dummy reason',
                                 domain_or_ip='192.168.0.1',
                                 pgp_key='Dummy PGP Key')

        CvdReport.objects.create(officer='Officer2',
                                 vulnerability_type='xss',
                                 explanation='Another dummy explanation',
                                 vulnerability_reason='Another dummy reason',
                                 domain_or_ip='192.168.0.2',
                                 pgp_key='Another dummy PGP Key')

        # Return all CvdReport objects
        return CvdReport.objects.all()


class CVDDetailView(LoginRequiredMixin, generic.DetailView):
    model = CvdReport
    # Update with your actual detail template
    template_name = 'cvd_service/cvd_detail.html'


class CVDCreateView(LoginRequiredMixin, generic.CreateView):
    model = CvdReport
    fields = ['officer', 'first_name', 'last_name', 'email', 'phone', 'vulnerability_type',
              'explanation', 'vulnerability_reason', 'domain_or_ip', 'pgp_key']
    template_name = 'cvd_service/create_cvd.html'
    success_url = reverse_lazy('cvd_service:cvd_list')


@require_POST
def delete_cvd(request, pk):
    cvd = get_object_or_404(CvdReport, pk=pk)
    cvd.delete()
    return redirect('cvd_service:cvd_list')
