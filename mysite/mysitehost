from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse(f"Хост сервера: {request.get_host()}<br />"
                        f"Браузер клиента: {request.META['HTTP_USER_AGENT']}<br />"
                        f"IP-адрес клиента: {request.META['REMOTE_ADDR']}")

def error(request):
    return HttpResponse(status=400, content="К сожалению произошла ошибка")

def user(request, login='default', folder='default', number=0):
    return HttpResponse(f"Логин пользователя: {login}<br />"
                        f"Имя папки с постами: {folder}<br />"
                        f"Номер поста: {number}")
