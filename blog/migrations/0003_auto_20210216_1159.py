# Generated by Django 3.1.4 on 2021-02-16 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20201216_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='user',
            field=models.IntegerField(blank=True, default=1, verbose_name='Автор'),
        ),
    ]
