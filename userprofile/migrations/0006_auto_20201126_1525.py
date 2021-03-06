# Generated by Django 3.1.3 on 2020-11-26 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0005_auto_20201126_1519'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdoctor',
            name='avatar',
        ),
        migrations.RemoveField(
            model_name='userdoctor',
            name='city',
        ),
        migrations.RemoveField(
            model_name='userdoctor',
            name='fio',
        ),
        migrations.RemoveField(
            model_name='userdoctor',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='userdoctor',
            name='skype',
        ),
        migrations.RemoveField(
            model_name='userdoctor',
            name='usertype',
        ),
        migrations.RemoveField(
            model_name='userdoctor',
            name='whatsapp',
        ),
        migrations.AddField(
            model_name='userdoctor',
            name='consultant',
            field=models.BooleanField(default=True, verbose_name='Я консультант'),
        ),
        migrations.AddField(
            model_name='userdoctor',
            name='doctor',
            field=models.BooleanField(default=True, verbose_name='Я врач'),
        ),
        migrations.AddField(
            model_name='userdoctor',
            name='orgtype',
            field=models.CharField(choices=[('ur', 'Юридическое лицо'), ('fiz', 'Физическое лицо')], max_length=11, null=True, verbose_name='Тип организации'),
        ),
    ]
