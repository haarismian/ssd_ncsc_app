from django.db import models


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

    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField()  # Email is now required
    phone = models.CharField(max_length=20, blank=True, null=True)
    vulnerability_type = models.CharField(
        max_length=30, choices=VULNERABILITY_TYPES)  # Vulnerability type is now required
    explanation = models.TextField()  # Explanation is now required
    vulnerability_reason = models.TextField()  # Reason is now required
    domain_or_ip = models.TextField()  # Domain/IP is now required
    pgp_key = models.TextField()

    def __str__(self):
        return f"CVD Report #{self.pk}"
