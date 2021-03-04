# Generated by Django 3.1.3 on 2020-12-08 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0023_auto_20201208_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdoctor',
            name='author',
            field=models.BooleanField(blank=True, verbose_name='Я автор видеолекций'),
        ),
        migrations.AlterField(
            model_name='userdoctor',
            name='consultant',
            field=models.BooleanField(blank=True, verbose_name='Я консультант'),
        ),
        migrations.AlterField(
            model_name='userdoctor',
            name='doctor',
            field=models.BooleanField(blank=True, verbose_name='Я врач'),
        ),
        migrations.AlterField(
            model_name='userdoctor',
            name='fullDoctor',
            field=models.BooleanField(blank=True, verbose_name='Я врач и консультант'),
        ),
        migrations.AlterField(
            model_name='userdoctor',
            name='orgtype',
            field=models.CharField(blank=True, choices=[('ur', 'Юридическое лицо'), ('fiz', 'Физическое лицо')], max_length=11, verbose_name='Тип организации'),
        ),
        migrations.AlterField(
            model_name='userdoctor',
            name='patientChildren',
            field=models.BooleanField(blank=True, verbose_name='Дети'),
        ),
        migrations.AlterField(
            model_name='userdoctor',
            name='patientGrown',
            field=models.BooleanField(blank=True, verbose_name='Взрослые'),
        ),
        migrations.AlterField(
            model_name='userdoctor',
            name='specialty',
            field=models.CharField(blank=True, max_length=100, verbose_name='Специализация'),
        ),
        migrations.AlterField(
            model_name='usermain',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='images/users', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='usermain',
            name='city',
            field=models.CharField(blank=True, max_length=100, verbose_name='Город'),
        ),
        migrations.AlterField(
            model_name='usermain',
            name='dob',
            field=models.CharField(blank=True, max_length=100, verbose_name='Дата рождения'),
        ),
        migrations.AlterField(
            model_name='usermain',
            name='fio',
            field=models.CharField(blank=True, max_length=100, verbose_name='ФИО'),
        ),
        migrations.AlterField(
            model_name='usermain',
            name='gender',
            field=models.CharField(blank=True, choices=[('male', 'Мужской'), ('female', 'Женский')], max_length=11, verbose_name='Пол'),
        ),
        migrations.AlterField(
            model_name='usermain',
            name='skype',
            field=models.CharField(blank=True, max_length=100, verbose_name='Skype'),
        ),
        migrations.AlterField(
            model_name='usermain',
            name='time_zone',
            field=models.CharField(blank=True, choices=[('(UTC +3) Москва, Санкт-Петербург, Воронеж, Казань', '(UTC +3) Москва, Санкт-Петербург, Воронеж, Казань'), ('(UTC +7): Республика Алтай, Алтайский край, Новосибирская, Омская, Томская области', '(UTC +7): Республика Алтай, Алтайский край, Новосибирская, Омская, Томская области')], max_length=150, verbose_name='Временная зона'),
        ),
        migrations.AlterField(
            model_name='usermain',
            name='whatsapp',
            field=models.CharField(blank=True, max_length=100, verbose_name='WhatsApp'),
        ),
    ]