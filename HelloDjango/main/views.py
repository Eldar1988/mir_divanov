from django.shortcuts import render
from .models import Social, Slide, About, Service, Team, Contact


def home(request):
    """Главная страница"""
    socials = Social.objects.all()
    slides = Slide.objects.order_by('order')

    return render(request, 'home.html', {
        'socials': socials,
        'slides': slides,
    })


def about(request):
    """Страница о нас"""
    about = About.objects.last()
    service = Service.objects.all()
    team = Team.objects.all()
    info_seo = about.info[3:165]

    return render(request, 'about.html', {
        'about': about,
        'service': service,
        'team': team,
        'info_seo': info_seo,
    })


def contacts(request):
    """Страница контакты"""
    contacts = Contact.objects.last()
    socials = Social.objects.all()

    return render(request, 'contacts.html', {
        'contacts': contacts,
        'socials': socials,
    })
