# Generated by Django 2.2.7 on 2021-06-29 21:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advertisement', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobalert',
            name='company_phone',
        ),
    ]