# Generated by Django 3.2.15 on 2022-11-01 21:50

import datetime
from django.conf import settings
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('social', '0041_alter_post_created_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='friend_request',
            field=models.ManyToManyField(blank=True, related_name='friend_request', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 1, 21, 50, 58, 493719, tzinfo=utc)),
        ),
    ]