from django.shortcuts import render
from django.views import generic
from .models import CvdReport
from django.utils import timezone

# Create your views here.


class IndexView(generic.ListView):
    template_name = "ncsc_cvd/index.html"

    def get_queryset(self):

        return CvdReport.objects.filter()
