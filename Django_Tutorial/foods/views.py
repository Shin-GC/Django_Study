from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(request, "foods/index.html")


def hello_view(request):
    return HttpResponse('<h1>Hola! hello 페이지 입니다 :)</h1>')