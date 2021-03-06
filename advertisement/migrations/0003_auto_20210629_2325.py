# Generated by Django 2.2.7 on 2021-06-29 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisement', '0002_remove_jobalert_company_phone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jobalert',
            old_name='phone',
            new_name='company_logo',
        ),
        migrations.AlterField(
            model_name='jobalert',
            name='company_email',
            field=models.EmailField(blank=True, max_length=254),
        ),
    ]
