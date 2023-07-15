from django.views.generic import TemplateView
from django.http import JsonResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView as AuthLoginView
from django.contrib.auth.views import LogoutView as AuthLogoutView
from django.core.cache import cache
from django.conf import settings

import logging
from django.shortcuts import render, redirect

logger = logging.getLogger(__name__)


class LoginView(AuthLoginView):
    def form_invalid(self, form):
        username = self.request.POST.get('username')
        ip = get_client_ip(self.request)
        cache_key = f"login_attempts:{ip}"
        login_attempts = cache.get(cache_key, 0)

        # Check if the user has reached the maximum login attempts
        if login_attempts >= 5:
            # Perform IP blocking logic here
            # You can use a library like django-ipware to block the IP

            # Set a flag in the session to display the banner
            self.request.session['login_attempts_exceeded'] = True

            # Log a warning indicating that the user has been blocked
            logger.warning(
                'User blocked due to exceeded login attempts - Username: %s, IP address: %s',
                username,
                ip
            )

            # Redirect the user to the login page
            return redirect('login')

        # Increment the login attempts counter
        cache.set(cache_key, login_attempts + 1,
                  settings.LOGIN_ATTEMPTS_CACHE_TIMEOUT)

        try:
            logger.warning(
                'Failed login attempt - Username: %s, IP address: %s',
                username,
                ip
            )
        except Exception as e:
            logger.error('Error in LoginView.form_invalid: %s', e)

        return self.render_to_response(self.get_context_data(form=form))


class LogoutView(AuthLogoutView):
    def dispatch(self, request, *args, **kwargs):
        try:
            username = self.request.user.username
            ip = get_client_ip(self.request)
            logger.info(
                'User logged out - Username: %s, IP address: %s',
                username,
                ip
            )
        except Exception as e:
            logger.error('Error in LogoutView.dispatch: %s', e)
        return super().dispatch(request, *args, **kwargs)


def get_client_ip(request):
    """Get client IP from request"""
    try:
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            # if it is a list, take first IP
            ip = x_forwarded_for.split(',')[0]
        else:
            # else take IP provided by Django
            ip = request.META.get('REMOTE_ADDR')
    except Exception as e:
        logger.error('Error in get_client_ip: %s', e)
        ip = None
    return ip


def index(request):
    try:
        return render(request, 'base_app/index.html')
    except Exception as e:
        logger.error('Error in index view: %s', e)
        raise


def register(request):
    try:
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('login')
        else:
            form = UserCreationForm()
        return render(request, 'registration/register.html', {'form': form})
    except Exception as e:
        logger.error('Error in register view: %s', e)


def cookie_consent(request):
    request.session['cookie_consent'] = True
    return JsonResponse({'status': 'ok'})


def privacy_policy(request):
    return render(request, 'base_app/privacy_policy.html')
