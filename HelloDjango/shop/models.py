import os
from uuid import uuid4

from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.urls import reverse


def path_and_rename(path, prefix):
    def wrapper(instance, filename):
        ext = filename.split(".")[-1]
        # get filename
        filename = "{}.{}.{}".format(prefix, uuid4().hex, ext)
        # return the whole path to the file
        return os.path.join(path, filename)
        return wrapper


class ShopInfo(models.Model):
    """Заголовок и текст ктатлога"""
    title = models.CharField('Загаловок каталога', max_length=255)
    text = models.TextField('Текст под заголовком')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Заголовок каталога'
        verbose_name_plural = 'Заголовок каталога'


class Category(models.Model):
    """Категории"""
    order = models.PositiveSmallIntegerField('Порядковый номер', default=0)
    title = models.CharField('Название категории', max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('order',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Image(models.Model):
    """Картинки"""
    image = models.ImageField('Фото товара', upload_to=path_and_rename("product_images/", 'slide'))
    title = models.CharField('Заголовок (для СЕО)', max_length=150)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Фото товара'
        verbose_name_plural = 'Фото товара'


class Product(models.Model):
    """Товар"""
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField('Название товара', max_length=255)
    price = models.CharField('Цена товара', max_length=100)
    material = models.CharField('Материал', max_length=255)
    short_description = models.TextField('Краткое описание')
    description = RichTextUploadingField('Полное описание')
    image = models.ImageField('Фото товара', upload_to=path_and_rename("product_images/", 'slide'))
    images = models.ManyToManyField(Image, verbose_name='Дополнительные фото', blank=True)

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'pk': self.id})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class NewOrder(models.Model):
    """Заказ"""
    name = models.CharField('Имя', max_length=255)
    product = models.CharField('Название товара', max_length=255, null=True, blank=True)
    phone = models.CharField('Телефон', max_length=30)
    comment = models.TextField('Комментарий', blank=True)
    create_date = models.DateTimeField('Дата создания', auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class TelegramBot(models.Model):
    """Настройки телеграм бота"""
    url = models.URLField('url')
    chat_id = models.CharField('chat id', max_length=100)

    class Meta:
        verbose_name = 'Телеграм бот'
        verbose_name_plural = 'Телеграм бот'