from django.urls import path

from . import views
from .views import CaseListView, CaseCreateView

app_name = "cases_service"
urlpatterns = [

    path("", views.CaseListView.as_view(),
         name='case_list'),  # Cases service index
    # Case detail for a given case the user clicks on
    path('<int:pk>/', views.CaseDetailView.as_view(), name='case_detail'),
    # POST endpoint for when a user wants to delete a case
    path('<str:id>/delete/', views.delete_case, name='delete_case'),
    # POST endpoint for when a user wants to create a case
    path('create/', views.CaseCreateView.as_view(), name='create_case'),

]
