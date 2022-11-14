# Generated by Django 3.2.15 on 2022-10-31 19:42

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0028_alter_post_created_on'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='date',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='friend_to',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='status',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='user_to',
        ),
        migrations.AlterField(
            model_name='post',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 31, 19, 42, 18, 510108, tzinfo=utc)),
        ),
    ]