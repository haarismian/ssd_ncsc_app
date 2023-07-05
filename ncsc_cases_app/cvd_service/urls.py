from django.urls import path

from . import views

app_name = "cvd_service"
urlpatterns = [
    path("", views.CVDListView.as_view(), name='cvd_list'),
    path('cvd/<int:pk>/', views.CVDDetailView.as_view(), name='cvd_detail'),
    path('cvd/<int:pk>/delete/', views.delete_cvd, name='delete_cvd'),
    path('create/', views.CVDCreateView.as_view(), name='create_cvd'),
]
