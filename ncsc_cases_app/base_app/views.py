from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView as AuthLoginView
import logging
from django.shortcuts import render, redirect

logger = logging.getLogger(__name__)


class LoginView(AuthLoginView):
    def form_invalid(self, form):
        logger.warning(
            'Failed login attempt - Username: %s, IP address: %s',
            self.request.POST['username'],
            get_client_ip(self.request)  # function to get client IP
        )
        return super().form_invalid(form)


def get_client_ip(request):
    """Get client IP from request"""
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]  # if it is a list, take first IP
    else:
        ip = request.META.get('REMOTE_ADDR')  # else take IP provided by Django
    return ip


def index(request):
    return render(request, 'base_app/index.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
