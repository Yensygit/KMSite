# Generated by Django 3.2.15 on 2022-10-10 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0005_alter_gallery_upload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='upload',
            field=models.FileField(upload_to='', verbose_name='Добавить фото'),
        ),
    ]
