# Generated by Django 3.1 on 2020-08-23 15:36

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='service',
            options={'verbose_name': 'Блок с иконками', 'verbose_name_plural': 'Блоки с иконками (страница о нас)'},
        ),
        migrations.RemoveField(
            model_name='about',
            name='image',
        ),
        migrations.AlterField(
            model_name='about',
            name='info',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Информация о компании'),
        ),
    ]