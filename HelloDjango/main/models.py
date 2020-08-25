import os
from uuid import uuid4

from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models


def path_and_rename(path, prefix):
    def wrapper(instance, filename):
        ext = filename.split(".")[-1]
        # get filename
        filename = "{}.{}.{}".format(prefix, uuid4().hex, ext)
        # return the whole path to the file
        return os.path.join(path, filename)
        return wrapper


class Slide(models.Model):
    """Слайдер"""
    order = models.PositiveSmallIntegerField('Подряковый номер', unique=True)
    title = models.CharField('Заголовок слайда', max_length=255)
    sub_title = models.CharField('Текст надо заголовом (необязательно)', max_length=150, blank=True)
    image = models.ImageField('Картинка', upload_to=path_and_rename("slides/", 'slide'),
                              help_text='Желательно оптимизировать на сайте https://tinypng.com/')
    btn_text = models.CharField('Текст - приглашение', max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Слайд'
        verbose_name_plural = 'Слайды'


class Service(models.Model):
    """Блоки с иконками"""
    title = models.CharField('Заголовок', max_length=255)
    text = models.TextField('Описание', max_length=1000)
    icon = models.CharField('Иконка', max_length=255, help_text='https://fontawesome.com/icons?d=gallery')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Блок с иконками'
        verbose_name_plural = 'Блоки с иконками (страница о нас)'


class Team(models.Model):
    """Команда"""
    name = models.CharField('Имя', max_length=255)
    icon = models.CharField('Должность', max_length=255)
    image = models.ImageField('Фото (в книжном формате)', upload_to=path_and_rename("team/", 'team'),
                              help_text='Желательно оптимизировать на сайте https://tinypng.com/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'


class Logo(models.Model):
    """Логотип"""
    logo = models.ImageField('Логотип', upload_to='logo/')

    class Meta:
        verbose_name = 'Логотип'
        verbose_name_plural = 'Логотип'


class About(models.Model):
    """Информация о компании"""
    title = models.CharField('Заголовок', max_length=255)
    sub_title = models.TextField('Текст под заголовком', max_length=1000)
    service_title = models.CharField('Заголовок блока с иконками', max_length=100)
    info_title = models.CharField('Заголовок блока с информацией', max_length=255)
    info = RichTextUploadingField('Информация о компании')
    team_title = models.CharField('Заголовок блока с командой', max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Информация о компании'
        verbose_name_plural = 'Информация о компании'


class Social(models.Model):
    """Социальные сети"""
    icon = models.CharField('Иконка', max_length=255, help_text='https://fontawesome.com/icons?d=gallery')
    url = models.URLField('Полная ссылка на страницу компании в соц сети')

    def __str__(self):
        return self.url

    class Meta:
        verbose_name = 'Социальная сеть'
        verbose_name_plural = 'Социальные сети'


class Contact(models.Model):
    """Контакты компании"""
    title = models.CharField('Заголовок страницы с контактами', max_length=255)
    sub_title = models.TextField('Текст под заголовком', max_length=1000)
    address = models.CharField('Адрес', max_length=255)
    map_iframe = models.TextField('Код с Google карты')
    email = models.EmailField('Email')
    phone = models.CharField('Телефон', max_length=30)
    whatsapp = models.CharField('Whatsapp (без 8, пробелов и символов)', max_length=30)
    social = models.ManyToManyField(Social, verbose_name='Соцсети')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Контакты'
        verbose_name_plural = 'Контакты'
