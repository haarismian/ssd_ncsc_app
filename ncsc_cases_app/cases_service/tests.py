from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Case
from django.contrib.auth import get_user_model


class CasesViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='johndoe', email='john@example.com', password='password')
        self.case = Case.objects.create(
            title='Test Case',
            description='This is a test case',
            user=self.user)

    def test_CaseListView(self):
        response = self.client.get(reverse('cases_service:case_list'))
        self.assertEqual(response.status_code, 200)
        queryset = response.context['cases']
        expected_objects = [str(obj) for obj in queryset]
        self.assertQuerysetEqual(queryset, expected_objects, transform=str)

    def test_CaseDetailView_valid(self):
        self.client.login(username='johndoe', password='password')
        response = self.client.get(
            reverse('cases_service:case_detail', args=(self.case.id,)))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['case'], self.case)

    def test_CaseDetailView_invalid(self):
        self.client.login(username='johndoe', password='password')
        response = self.client.get(
            reverse('cases_service:case_detail', args=(999,)))
        self.assertEqual(response.status_code, 404)

    def test_CaseCreateView(self):
        self.client.login(username='johndoe', password='password')
        response = self.client.post(reverse('cases_service:create_case'), {
            'title': 'New Case',
            'description': 'This is a new case',
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Case.objects.count(), 2)
        self.assertEqual(Case.objects.last().title, 'New Case')

    def test_CaseCreateView_no_data(self):
        self.client.login(username='johndoe', password='password')
        response = self.client.post(reverse('cases_service:create_case'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Case.objects.count(), 1)

    def test_delete_case(self):
        self.client.login(username='johndoe', password='password')
        response = self.client.post(
            reverse('cases_service:delete_case', args=(self.case.id,)))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Case.objects.count(), 0)

    def test_delete_case_invalid(self):
        self.client.login(username='johndoe', password='password')
        response = self.client.post(
            reverse('cases_service:delete_case', args=(999,)))
        self.assertEqual(response.status_code, 404)
        self.assertEqual(Case.objects.count(), 1)

    def test_CaseCreateView_not_logged_in(self):
        response = self.client.post(reverse('cases_service:create_case'), {
            'title': 'New Case',
            'description': 'This is a new case',
        })
        # Expecting a redirect to login page
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Case.objects.count(), 1)

    def test_delete_case_not_logged_in(self):
        response = self.client.post(
            reverse('cases_service:delete_case', args=(self.case.id,)))
        # Expecting a redirect to login page
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Case.objects.count(), 1)
