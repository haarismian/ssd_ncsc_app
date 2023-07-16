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
        """
        Handle the form submission when the form is invalid (failed login attempt).

        This method is called when the form data is invalid, i.e., the username or password is incorrect.
        It logs the failed login attempt and checks if the user has exceeded the maximum login attempts.
        If the user has exceeded the maximum login attempts, it performs IP blocking logic, sets a flag in the session
        to display the banner, logs a warning about the user being blocked, and redirects the user to the login page.
        If the user has not exceeded the maximum login attempts, it increments the login attempts counter in the cache,
        logs the failed login attempt, and renders the response with the form errors.

        Applicable reference(s):
        A07:2021 – Identification and Authentication Failures

        """

        username = self.request.POST.get('username')
        ip = get_client_ip(self.request)
        cache_key = f"login_attempts:{ip}"
        login_attempts = cache.get(cache_key, 0)

        # Check if the user has reached the maximum login attempts
        if login_attempts >= 5:
            # IP blocking logic
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
        """
        Handle the user logout.

        This method is called when the user logs out. It logs the username and IP address of the user who logged out.
        """
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
    """
    Get the client IP address from the request.

    This function retrieves the client's IP address from the request's META data.
    It checks if the request contains an X-Forwarded-For header and extracts the first IP address from the list.
    If the X-Forwarded-For header is not present, it retrieves the IP address provided by Django.

    Returns:
    - The client IP address.
    """
    try:
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            # if it is a list, take the first IP
            ip = x_forwarded_for.split(',')[0]
        else:
            # else take the IP provided by Django
            ip = request.META.get('REMOTE_ADDR')
    except Exception as e:
        logger.error('Error in get_client_ip: %s', e)
        ip = None
    return ip


def index(request):
    """
    Render the index page.

    This view renders the index page.
    """
    try:
        return render(request, 'base_app/index.html')
    except Exception as e:
        logger.error('Error in index view: %s', e)
        raise


def register(request):
    """
    Handle user registration.

    This view handles the user registration process.
    If the request method is POST, it validates the registration form.
    If the form is valid, it saves the user and redirects to the login page.
    If the form is not valid, it renders the registration form with the form errors.

    Applicable reference(s):
    OAT-019 Account Creation
    """
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
    """
    Set the cookie consent flag.

    This view sets the cookie consent flag in the user's session.
    It returns a JSON response with the status 'ok'.

    Applicable reference(s):
    https://gdpr.eu/cookies/
    """
    request.session['cookie_consent'] = True
    return JsonResponse({'status': 'ok'})


def privacy_policy(request):
    """
    Render the privacy policy page.

    This view renders the privacy policy page.
    """
    return render(request, 'base_app/privacy_policy.html')
