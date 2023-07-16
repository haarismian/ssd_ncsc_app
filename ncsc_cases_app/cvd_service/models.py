from django.db import models
from django_cryptography.fields import encrypt


class CvdReport(models.Model):
    VULNERABILITY_TYPES = (
        ('injection', 'Injection'),
        ('broken_auth', 'Broken Authentication'),
        ('data_exposure', 'Sensitive Data Exposure'),
        ('xxe', 'XML External Entities (XXE)'),
        ('misconfigurations', 'Security Misconfigurations'),
        ('xss', 'Cross-Site Scripting (XSS)'),
        ('access_control', 'Broken Access Control'),
        ('insecure_deserialization', 'Insecure Deserialization'),
        ('availability', 'Availability'),
        ('integrity', 'Integrity'),
        ('confidentiality', 'Confidentiality'),
    )

    """
    Applicable reference(s):
    A3:2017-Sensitive Data Exposure

    """
    first_name = encrypt(models.CharField(
        max_length=100, blank=True, null=True))
    last_name = encrypt(models.CharField(
        max_length=100, blank=True, null=True))
    email = encrypt(models.EmailField())  # Email is required
    phone = encrypt(models.CharField(max_length=20, blank=True, null=True))
    vulnerability_type = models.CharField(
        max_length=30, choices=VULNERABILITY_TYPES)  # Vulnerability type is required
    explanation = models.TextField()  # Explanation is required
    vulnerability_reason = models.TextField()  # Reason is required
    domain_or_ip = models.TextField()  # Domain/IP is required
    pgp_key = encrypt(models.TextField())

    def __str__(self):
        return f"CVD Report #{self.pk}"
