from . import views
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views

app_name = "base_app"
urlpatterns = [
    # Index URL
    path('', views.index, name='home'),

    # URLs for cases and cvd services

    path("cases/", include("cases_service.urls")),
    path("cvd/", include("cvd_service.urls")),

    path('cookie-consent/', views.cookie_consent, name='cookie_consent'),
    path('privacy_policy/', views.privacy_policy, name='privacy_policy'),

    path("admin/", admin.site.urls),

    path('accounts/login/', views.LoginView.as_view(), name='login'),
    path('accounts/logout/', views.LogoutView.as_view(), name='logout'),
    path('accounts/password_change/',
         auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('accounts/password_change/done/',
         auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('accounts/password_reset/',
         auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('accounts/password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('accounts/reset/done/', auth_views.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),

    path('register/', views.register, name='register'),


]
