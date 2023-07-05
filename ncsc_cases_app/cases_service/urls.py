from django.urls import path

from . import views
from .views import CaseListView, CaseCreateView

app_name = "cases"
urlpatterns = [
    path("", views.CaseListView.as_view(), name='case_list'),
    path('<str:id>/delete/', views.delete_case, name='delete_case'),
    path('create/', views.CaseCreateView.as_view(), name='create_case'),


    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),



]
