from django.urls import path

from . import views
from .views import CaseListView, CaseCreateView

app_name = "cases_service"
urlpatterns = [
    path("", views.CaseListView.as_view(), name='case_list'),
    path('<int:pk>/', views.CaseDetailView.as_view(), name='case_detail'),
    path('<str:id>/delete/', views.delete_case, name='delete_case'),
    path('create/', views.CaseCreateView.as_view(), name='create_case'),

]
