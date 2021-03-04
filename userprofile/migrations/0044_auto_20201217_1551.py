# Generated by Django 3.1.3 on 2020-12-17 12:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('userprofile', '0043_auto_20201216_1759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermain',
            name='city',
            field=models.CharField(blank=True, max_length=200, verbose_name='Город'),
        ),
        migrations.AlterField(
            model_name='usermain',
            name='dob',
            field=models.CharField(blank=True, max_length=10, verbose_name='Дата рождения'),
        ),
        migrations.AlterField(
            model_name='usermain',
            name='gender',
            field=models.CharField(blank=True, choices=[('male', 'Мужской'), ('female', 'Женский')], max_length=6, verbose_name='Пол'),
        ),
        migrations.AlterField(
            model_name='usermain',
            name='phone',
            field=models.CharField(blank=True, max_length=20, verbose_name='Номер телефона'),
        ),
        migrations.AlterField(
            model_name='usermain',
            name='time_zone',
            field=models.CharField(blank=True, choices=[('UTC +3', '(UTC +3) Москва, Санкт-Петербург, Воронеж, Казань'), ('UTC +7', '(UTC +7): Республика Алтай, Алтайский край, Новосибирская, Омская, Томская области'), ('UTC +4', 'wefwefwefwefwef'), ('UTC +9', '(UTC +9) Какой то город')], max_length=200, verbose_name='Временная зона'),
        ),
        migrations.AlterField(
            model_name='usermain',
            name='user',
            field=models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]