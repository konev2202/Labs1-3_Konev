from django.http import HttpResponse
from django.shortcuts import render
from django import template  


def home(request):
    # теперь вместо текста возвращаем HTML-шаблон
    return render(request, 'templates/static_handler.html')


def hello(request):
    # hello можно оставить как простой текст
    return HttpResponse("Привет, Мир!")
