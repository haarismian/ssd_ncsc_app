from django.test import TestCase, Client, RequestFactory
from django.contrib.auth.models import AnonymousUser, User
from django.core.exceptions import ValidationError
from django.urls import reverse
from .models import CvdReport
from .views import CVDListView, CVDDetailView, CVDCreateView, delete_cvd


class CvdReportTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.user = User.objects.create_user(
            username='johndoe', email='john@example.com', password='password')
        self.cvdreport = CvdReport.objects.create(
            first_name="John",
            last_name="Doe",
            email="john@example.com",
            phone="1234567890",
            vulnerability_type="broken_auth",
            explanation="Test explanation",
            vulnerability_reason="Test vulnerability reason",
            domain_or_ip="192.0.2.0",
            pgp_key="Test PGP Key"
        )

    def test_invalid_vulnerability_type(self):
        with self.assertRaises(ValidationError):
            # Attempt to create a CvdReport instance with an invalid vulnerability type
            invalid_cvdreport = CvdReport(
                first_name="John",
                last_name="Doe",
                email="john@example.com",
                phone="1234567890",
                vulnerability_type="Invalid vulnerability type",
                explanation="Test explanation",
                vulnerability_reason="Test vulnerability reason",
                domain_or_ip="192.0.2.0",
                pgp_key="Test PGP Key"
            )
            invalid_cvdreport.full_clean()

    def test_CVDListView_get_queryset(self):
        self.client.login(username='johndoe', password='password')
        # Send a GET request to the cvd_list URL
        response = self.client.get(reverse('cvd_service:cvd_list'))
        self.assertEqual(response.status_code, 200)
        # Compare the queryset of CvdReport objects in the context with the expected queryset
        self.assertQuerysetEqual(
            response.context['cvd_list'],
            CvdReport.objects.all(),
            transform=lambda x: x  # compare the objects directly
        )

    def test_CVDDetailView(self):
        self.client.login(username='johndoe', password='password')
        # Request the detail view for a specific CvdReport instance
        response = self.client.get(
            reverse('cvd_service:cvd_detail', args=(self.cvdreport.id,)))
        self.assertEqual(response.status_code, 200)
        # Ensure the cvdreport object in the context matches the expected CvdReport instance
        self.assertEqual(response.context['cvdreport'], self.cvdreport)

    def test_CVDCreateView(self):
        self.client.login(username='johndoe', password='password')
        # Send a POST request to the create_cvd URL with form data
        response = self.client.post(reverse('cvd_service:create_cvd'), {
            'first_name': 'Jane',
            'last_name': 'Doe',
            'email': 'jane@example.com',
            'phone': '0987654321',
            'vulnerability_type': 'insecure_deserialization',
            'explanation': 'Test explanation',
            'vulnerability_reason': 'Test vulnerability reason',
            'domain_or_ip': '192.0.2.0',
            'pgp_key': 'Test PGP Key'
        })
        self.assertEqual(response.status_code, 302)
        # Ensure the number of CvdReport objects has increased by 1
        self.assertEqual(CvdReport.objects.count(), 2)
        # Verify that the last CvdReport object created has the expected first_name value
        self.assertEqual(CvdReport.objects.last().first_name, 'Jane')

    def test_delete_cvd(self):
        self.client.login(username='johndoe', password='password')
        # Send a POST request to delete a specific CvdReport instance
        response = self.client.post(
            reverse('cvd_service:delete_cvd', args=(self.cvdreport.id,)))
        self.assertEqual(response.status_code, 302)
        # Ensure the CvdReport instance has been deleted (count is 0)
        self.assertEqual(CvdReport.objects.count(), 0)
