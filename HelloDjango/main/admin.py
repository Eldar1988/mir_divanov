from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Slide, Service, Team, About, Social, Contact, Logo


@admin.register(Slide)
class SlideAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    list_editable = ('order',)
    save_as = True

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50"')

    get_image.short_description = 'Миниатюра'


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon')
    list_editable = ('icon',)
    save_as = True


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon')
    list_editable = ('icon',)


@admin.register(Social)
class SocialAdmin(admin.ModelAdmin):
    list_display = ('id', 'icon', 'url')
    list_editable = ('icon', 'url')


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('title', 'address', 'email', 'phone')
    list_editable = ('address', 'email', 'phone')


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('title',)


admin.site.register(Logo)

admin.site.site_title = 'Мир диванов'
admin.site.site_header = 'Мир диванов - администрирование'
