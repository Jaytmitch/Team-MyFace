# Generated by Django 3.2.15 on 2022-10-31 19:31

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('social', '0026_alter_post_created_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='friend_to',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='friend_to', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='status',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user_to',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_to', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 31, 19, 31, 29, 673458, tzinfo=utc)),
        ),
    ]