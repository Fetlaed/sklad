# Generated by Django 2.2.5 on 2019-09-28 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='position',
            field=models.CharField(choices=[('Грузчик', 'Грузчик'), ('Менеджер', 'Менеджер'), ('Администратор', 'Администратор')], default='Грузчик', max_length=30, verbose_name='Должность'),
        ),
    ]
