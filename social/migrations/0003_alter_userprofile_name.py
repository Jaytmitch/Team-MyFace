# Generated by Django 3.2.15 on 2022-10-04 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0002_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='name',
            field=models.CharField(max_length=30, null=True, verbose_name=True),
        ),
    ]
