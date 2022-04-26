from django.shortcuts import render
from django.urls import reverse
import json

with open('data.txt') as json_file:
    product_list = json.load(json_file)

MENU_LINKS = {
    'index': 'Главная',
    'products': 'Продукты',
    'contact': 'Контакты',
}


def main(request):
    return render(request, 'mainapp/index.html', context={
        'title': 'Главная',
        'menu': MENU_LINKS,
    })


def products(request):
    return render(request, 'mainapp/products.html', context={
        'title': 'Продукты',
        'menu': MENU_LINKS,
        'products': product_list,
    })


def contact(request):
    return render(request, 'mainapp/contact.html', context={
        'title': 'Контакты',
        'menu': MENU_LINKS,
    })
