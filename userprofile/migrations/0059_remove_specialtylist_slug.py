# Generated by Django 3.1.4 on 2021-02-04 07:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0058_specialtylist_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='specialtylist',
            name='slug',
        ),
    ]
