# Generated by Django 4.2.2 on 2023-07-05 22:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cases_service', '0003_remove_case_case_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
