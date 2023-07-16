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
        """
        Test the CaseListView.

        This test verifies that the CaseListView returns a status code of 200 (OK).
        It checks that the queryset of cases in the response context matches the expected objects.
        """
        response = self.client.get(reverse('cases_service:case_list'))
        self.assertEqual(response.status_code, 200)
        queryset = response.context['cases']
        expected_objects = [str(obj) for obj in queryset]
        self.assertQuerysetEqual(queryset, expected_objects, transform=str)

    def test_CaseDetailView_valid(self):
        """
        Test the CaseDetailView with a valid case ID.

        This test verifies that the CaseDetailView returns a status code of 200 (OK) for a valid case ID.
        It checks that the case object in the response context matches the expected case.
        """
        self.client.login(username='johndoe', password='password')
        response = self.client.get(
            reverse('cases_service:case_detail', args=(self.case.id,)))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['case'], self.case)

    def test_CaseDetailView_invalid(self):
        """
        Test the CaseDetailView with an invalid case ID.

        This test verifies that the CaseDetailView returns a status code of 404 (Not Found) for an invalid case ID.
        """
        self.client.login(username='johndoe', password='password')
        response = self.client.get(
            reverse('cases_service:case_detail', args=(999,)))
        self.assertEqual(response.status_code, 404)

    def test_CaseCreateView(self):
        """
        Test the CaseCreateView with valid data.

        This test verifies that the CaseCreateView creates a new case with the provided data.
        It checks that the response status code is 302 (Redirect) and the case count increases by 1.
        It also checks that the title of the last created case matches the provided title.
        """
        self.client.login(username='johndoe', password='password')
        response = self.client.post(reverse('cases_service:create_case'), {
            'title': 'New Case',
            'description': 'This is a new case',
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Case.objects.count(), 2)
        self.assertEqual(Case.objects.last().title, 'New Case')

    def test_CaseCreateView_no_data(self):
        """
        Test the CaseCreateView with no data.

        This test verifies that the CaseCreateView returns a status code of 200 (OK) and does not create a new case
        when no data is provided.
        """
        self.client.login(username='johndoe', password='password')
        response = self.client.post(reverse('cases_service:create_case'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Case.objects.count(), 1)

    def test_delete_case(self):
        """
        Test the delete_case view with a valid case ID.

        This test verifies that the delete_case view deletes the case with the provided case ID.
        It checks that the response status code is 302 (Redirect) and the case count decreases by 1.
        """
        self.client.login(username='johndoe', password='password')
        response = self.client.post(
            reverse('cases_service:delete_case', args=(self.case.id,)))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Case.objects.count(), 0)

    def test_delete_case_invalid(self):
        """
        Test the delete_case view with an invalid case ID.

        This test verifies that the delete_case view returns a status code of 404 (Not Found) for an invalid case ID.
        """
        self.client.login(username='johndoe', password='password')
        response = self.client.post(
            reverse('cases_service:delete_case', args=(999,)))
        self.assertEqual(response.status_code, 404)
        self.assertEqual(Case.objects.count(), 1)
