# Generated by Django 4.2.2 on 2023-07-05 21:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cases_service', '0002_case'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='case',
            name='case_id',
        ),
    ]