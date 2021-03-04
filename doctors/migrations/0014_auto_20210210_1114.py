# Generated by Django 3.1.4 on 2021-02-10 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0013_auto_20210210_1043'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='star',
        ),
        migrations.AddField(
            model_name='review',
            name='star_pers',
            field=models.IntegerField(blank=True, default=0, verbose_name='Личные качества'),
        ),
        migrations.AddField(
            model_name='review',
            name='star_prof',
            field=models.IntegerField(blank=True, default=0, verbose_name='Профессионализм'),
        ),
    ]