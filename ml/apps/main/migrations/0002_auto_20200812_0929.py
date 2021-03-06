# Generated by Django 3.1 on 2020-08-12 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='mean',
            field=models.FloatField(default=0.0, verbose_name='guarda la mediana'),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='median',
            field=models.FloatField(default=0.0, verbose_name='guarda la media'),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='mode',
            field=models.FloatField(default=0.0, verbose_name='guarda la moda'),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='trimmed_mean',
            field=models.FloatField(default=0.0, verbose_name='guarda media recortada'),
        ),
    ]
