# Generated by Django 4.2.2 on 2023-07-06 21:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cvd_service', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cvdreport',
            name='officer',
        ),
    ]
