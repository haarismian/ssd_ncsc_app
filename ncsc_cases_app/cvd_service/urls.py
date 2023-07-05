from django.urls import path

from . import views

app_name = "cvd_service"
urlpatterns = [
    path("", views.CVDListView.as_view(), name='cvd_list'),
    path('<str:id>/delete/', views.delete_cvd, name='delete_cvd'),
    path('create/', views.CVDCreateView.as_view(), name='create_cvd'),
]
