from django.test import TestCase, Client, RequestFactory
from django.contrib.auth.models import AnonymousUser, User
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
            vulnerability_type="Test vulnerability type",
            explanation="Test explanation",
            vulnerability_reason="Test vulnerability reason",
            domain_or_ip="192.0.2.0",
            pgp_key="Test PGP Key"
        )

    def test_CVDListView_get_queryset(self):
        self.client.login(username='johndoe', password='password')
        response = self.client.get(reverse('cvd_service:cvd_list'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['cvd_list'], [
                                 '<CvdReport: CvdReport object (1)>'])

    def test_CVDDetailView(self):
        self.client.login(username='johndoe', password='password')
        response = self.client.get(
            reverse('cvd_service:cvd_detail', args=(self.cvdreport.id,)))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['cvdreport'], self.cvdreport)

    def test_CVDCreateView(self):
        self.client.login(username='johndoe', password='password')
        response = self.client.post(reverse('cvd_service:create_cvd'), {
            'first_name': 'Jane',
            'last_name': 'Doe',
            'email': 'jane@example.com',
            'phone': '0987654321',
            'vulnerability_type': 'Test vulnerability type',
            'explanation': 'Test explanation',
            'vulnerability_reason': 'Test vulnerability reason',
            'domain_or_ip': '192.0.2.0',
            'pgp_key': 'Test PGP Key'
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(CvdReport.objects.count(), 2)
        self.assertEqual(CvdReport.objects.last().first_name, 'Jane')

    def test_delete_cvd(self):
        self.client.login(username='johndoe', password='password')
        response = self.client.post(
            reverse('cvd_service:delete_cvd', args=(self.cvdreport.id,)))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(CvdReport.objects.count(), 0)
