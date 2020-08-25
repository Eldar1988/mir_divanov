from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Category, Product, Image, ShopInfo, NewOrder, TelegramBot

admin.site.register(ShopInfo)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'material', 'get_image')
    search_fields = ('name', 'material')
    list_filter = ('category',)
    list_editable = ('price', 'category', 'material')
    save_as = True
    save_on_top = True

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50"')

    get_image.short_description = 'Изображение'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(NewOrder)
class NewOrderAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'product', 'create_date')
    readonly_fields = ('name', 'phone', 'comment', 'product')


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_image')

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50"')

    get_image.short_description = 'Изображение'

admin.site.register(TelegramBot)
