# Generated by Django 2.2.7 on 2021-09-14 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0003_auto_20210912_2149'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category_en_us',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='category_it',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='category_pt',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
