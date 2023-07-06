from . import views
from django.contrib import admin
from django.urls import include, path

app_name = "base_app"
urlpatterns = [
    path('', views.index, name='my_page'),
    path("cases/", include("cases_service.urls")),
    path("cvd/", include("cvd_service.urls")),
    path("admin/", admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),


]
