# Generated by Django 2.1 on 2018-12-11 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notices', '0009_auto_20181211_2201'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='regnumber',
            name='eu',
        ),
        migrations.AddField(
            model_name='regnumber',
            name='env',
            field=models.BooleanField(default=0, verbose_name='Körny.védelem?'),
            preserve_default=False,
        ),
    ]