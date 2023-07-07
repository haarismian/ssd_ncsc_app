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
        response = self.client.post(
            self.url, {'username': self.username, 'password': self.password})

        # Update the expected URL to match the redirect URL
        expected_url = reverse('home')

        self.assertRedirects(response, expected_url=expected_url)

    def test_invalid_login(self):
        response = self.client.post(
            self.url, {'username': self.username, 'password': 'wrongpassword'})

        self.assertContains(
            response, 'Please enter a correct username and password')
