# Generated by Django 3.1 on 2020-08-24 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_remove_about_services'),
    ]

    operations = [
        migrations.CreateModel(
            name='Logo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(upload_to='logo/', verbose_name='Логотип')),
            ],
            options={
                'verbose_name': 'Логотип',
                'verbose_name_plural': 'Логотип',
            },
        ),
    ]
