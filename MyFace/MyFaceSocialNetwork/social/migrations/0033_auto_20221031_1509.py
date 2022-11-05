# Generated by Django 3.2.15 on 2022-10-31 20:09

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0032_alter_post_created_on'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='followers',
            new_name='friends',
        ),
        migrations.AlterField(
            model_name='post',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 31, 20, 8, 55, 271506, tzinfo=utc)),
        ),
    ]
