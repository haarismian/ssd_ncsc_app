# Generated by Django 4.2.2 on 2023-07-05 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CvdReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('officer', models.CharField(max_length=100)),
                ('first_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('vulnerability_type', models.CharField(choices=[('injection', 'Injection'), ('broken_auth', 'Broken Authentication'), ('data_exposure', 'Sensitive Data Exposure'), ('xxe', 'XML External Entities (XXE)'), ('misconfigurations', 'Security Misconfigurations'), ('xss', 'Cross-Site Scripting (XSS)'), ('access_control', 'Broken Access Control'), ('insecure_deserialization', 'Insecure Deserialization'), ('availability', 'Availability'), ('integrity', 'Integrity'), ('confidentiality', 'Confidentiality')], max_length=30)),
                ('explanation', models.TextField()),
                ('vulnerability_reason', models.TextField()),
                ('domain_or_ip', models.TextField()),
                ('pgp_key', models.TextField()),
            ],
        ),
    ]
