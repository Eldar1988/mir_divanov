# Generated by Django 3.1 on 2020-08-25 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_neworder_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='TelegramBot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(verbose_name='url')),
                ('chat_id', models.CharField(max_length=100, verbose_name='chat id')),
            ],
            options={
                'verbose_name': 'Телеграм бот',
                'verbose_name_plural': 'Телеграм бот',
            },
        ),
    ]