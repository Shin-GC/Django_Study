from django.shortcuts import render


def index(request):
    return render(request, "menus/index.html")


def detail(request, menu):
    return render(request, 'menus/detail.html')
