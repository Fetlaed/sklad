# Generated by Django 2.2.5 on 2019-09-28 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shelving', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shelving',
            name='size',
        ),
        migrations.AddField(
            model_name='shelving',
            name='lengthS',
            field=models.IntegerField(blank=True, null=True, verbose_name='Длина'),
        ),
        migrations.AddField(
            model_name='shelving',
            name='widthS',
            field=models.IntegerField(blank=True, null=True, verbose_name='Ширина'),
        ),
    ]
