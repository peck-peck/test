# Generated by Django 2.2.7 on 2021-09-12 20:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0002_auto_20210827_2354'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='category_en_us',
        ),
        migrations.RemoveField(
            model_name='category',
            name='category_it',
        ),
        migrations.RemoveField(
            model_name='category',
            name='category_pt',
        ),
    ]