# Generated by Django 2.2.7 on 2021-09-06 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0003_notification_post_view'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='post_view',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
