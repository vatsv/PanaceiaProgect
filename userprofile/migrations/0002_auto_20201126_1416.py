# Generated by Django 3.1.3 on 2020-11-26 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='city',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='fio',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
