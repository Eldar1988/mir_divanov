import requests
from django.shortcuts import render, redirect
from django.views.generic.base import View

from .forms import NewOrdertForm
from .models import Category, Product, ShopInfo, TelegramBot
from main.models import Contact


def catalog(request):
    """Страница каталог"""
    products = Product.objects.all()
    categories = Category.objects.all()
    info = ShopInfo.objects.last()
    return render(request, 'catalog.html', {
        'products': products,
        'info': info,
        'categories': categories,
    })


class ProductDetailView(View):
    """Страница товара"""
    def get(self, request, pk):
        product = Product.objects.get(id=pk)
        contact = Contact.objects.last()
        description = product.description[3:160]
        return render(request, 'product_detail.html', {
            'product': product,
            'contact': contact,
            'description': description,
        })


class CreateOrder(View):
    """Страница заказа товара"""
    def get(self, request, pk):
        product = Product.objects.get(id=pk)
        return render(request, 'order.html', {
            'product': product
        })

    def post(self, request, pk):
        form = NewOrdertForm(request.POST)
        bot = TelegramBot.objects.last()

        if form.is_valid():
            form.save()
            success = True

            url = f'{bot.url}' + '/sendMessage'
            chat_id = bot.chat_id
            product = request.POST.get('product')
            name = request.POST.get('name')
            phone = request.POST.get('phone')
            comment = request.POST.get('comment')
            price = request.POST.get('price')
            text = f'Новая заявка: \n Товар: {product} \n Цена: {price} \n Имя: {name} \n Телефон: {phone} \n Дополнительно: {comment}'

            answer = {'chat_id': chat_id, 'text': text}
            requests.post(url, answer)

            return render(request, 'thanks.html', {
                'success': success,
            })
        return redirect('product_detail')