from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


# Create your views here.


def index(request):
    today = str(datetime.today().date())
    context = {"date": today}
    return render(request, "foods/index.html", context=context)


def hello_view(request):
    return HttpResponse('<h1>Hola! hello 페이지 입니다 :)</h1>')
