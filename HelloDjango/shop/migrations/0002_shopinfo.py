# Generated by Django 3.1 on 2020-08-23 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShopInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Загаловок каталога')),
                ('text', models.TextField(verbose_name='Текст под заголовком')),
            ],
        ),
    ]
