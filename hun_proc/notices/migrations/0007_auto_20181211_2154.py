# Generated by Django 2.1 on 2018-12-11 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notices', '0006_regnumber_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='regnumber',
            name='amount',
            field=models.FloatField(max_length=50, null=True, verbose_name='Beszerzés Összege'),
        ),
        migrations.AddField(
            model_name='regnumber',
            name='asker',
            field=models.CharField(max_length=50, null=True, verbose_name='Ajánlatkérő'),
        ),
        migrations.AddField(
            model_name='regnumber',
            name='asker_act',
            field=models.CharField(max_length=50, null=True, verbose_name='Ajánlatkérő'),
        ),
        migrations.AddField(
            model_name='regnumber',
            name='asker_type',
            field=models.CharField(max_length=50, null=True, verbose_name='Ajánlatkérő'),
        ),
        migrations.AddField(
            model_name='regnumber',
            name='date',
            field=models.DateField(null=True, verbose_name='Közzététel dátuma'),
        ),
        migrations.AddField(
            model_name='regnumber',
            name='eu',
            field=models.BooleanField(default=0, verbose_name='Eus?'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='regnumber',
            name='name',
            field=models.CharField(max_length=50, null=True, verbose_name='Elnevezés'),
        ),
        migrations.AddField(
            model_name='regnumber',
            name='proc_type',
            field=models.CharField(max_length=50, null=True, verbose_name='Eljárás fajtája'),
        ),
    ]
