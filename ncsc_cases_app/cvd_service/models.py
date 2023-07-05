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

    officer = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    vulnerability_type = models.CharField(
        max_length=30, choices=VULNERABILITY_TYPES)
    explanation = models.TextField()
    vulnerability_reason = models.TextField()
    domain_or_ip = models.TextField()
    pgp_key = models.TextField()

    def __str__(self):
        return f"CVD Report #{self.pk}"
