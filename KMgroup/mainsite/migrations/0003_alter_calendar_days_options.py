# Generated by Django 3.2.15 on 2022-09-16 12:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0002_auto_20220916_1142'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='calendar_days',
            options={'verbose_name': 'событие', 'verbose_name_plural': 'События'},
        ),
    ]