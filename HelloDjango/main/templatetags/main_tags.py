from django import template
from ..models import Social, Contact, Logo

register = template.Library()


@register.simple_tag()
def get_socials():
    socials = Social.objects.all()
    return socials


@register.simple_tag()
def get_contacts():
    contacts = Contact.objects.last()
    return contacts


@register.simple_tag()
def get_logo():
    logo = Logo.objects.last()
    return logo

