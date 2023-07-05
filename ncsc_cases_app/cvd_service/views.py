from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from django.urls import reverse_lazy
from django.views import generic
from .models import CvdReport
from django.utils import timezone

# Create your views here.


class CVDListView(generic.ListView):
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


class CVDCreateView(generic.CreateView):
    model = CvdReport
    fields = ['officer', 'first_name', 'last_name', 'email', 'phone', 'vulnerability_type',
              'explanation', 'vulnerability_reason', 'domain_or_ip', 'pgp_key']
    template_name = 'cases_service/create_case.html'
    success_url = reverse_lazy('cvd_service:cvd_list')


# class DetailView(generic.DetailView):
#     model = Question
#     template_name = "cases_service/detail.html"

#     def get_queryset(self):
#         """
#         Excludes any questions that aren't published yet.
#         """
#         return Question.objects.filter(pub_date__lte=timezone.now())


@require_POST
def delete_cvd(request, id):
    case = CvdReport.objects.get(id=id)
    case.delete()
    return redirect('cvd_service:cvd_list')  # name of your cvd list URL
