# Generated by Django 3.1.4 on 2021-01-07 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='time',
            field=models.TimeField(default='00:00:00', max_length=100, verbose_name='Время'),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='data',
            field=models.DateField(blank=True, max_length=100, verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='doctor_id',
            field=models.IntegerField(blank=True, default=1, verbose_name='Доктор'),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='title',
            field=models.CharField(blank=True, max_length=100, verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='user_id',
            field=models.IntegerField(blank=True, default=1, verbose_name='Пациент'),
        ),
    ]