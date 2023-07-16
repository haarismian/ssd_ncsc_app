from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


class LoginViewTest(TestCase):
    def setUp(self):
        self.url = reverse('login')
        self.username = 'testuser'
        self.password = 'testpassword'
        User.objects.create_user(
            username=self.username, password=self.password)

    def test_valid_login(self):
        """
        Test for valid login attempt.
        This function verifies that a user can successfully log in with the correct username and password.
        It uses the `client.post` method to send a POST request to the login URL with the username and password.
        The expected behavior is a redirect to the home URL after successful login.
        """
        response = self.client.post(
            self.url, {'username': self.username, 'password': self.password})

        # Update the expected URL to match the redirect URL
        expected_url = reverse('home')

        self.assertRedirects(response, expected_url=expected_url)

    def test_invalid_login(self):
        """
        Test for invalid login attempt.
        This function verifies that an error message is displayed when an invalid username or password is provided.
        It uses the `client.post` method to send a POST request to the login URL with an incorrect password.
        The expected behavior is to display an error message indicating that the username or password is incorrect.
        """
        response = self.client.post(
            self.url, {'username': self.username, 'password': 'wrongpassword'})

        self.assertContains(
            response, 'Please enter a correct username and password')
