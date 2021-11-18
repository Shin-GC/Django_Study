from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse("<h2>Hello, Django</h2>")

def hello_view(request):
    return HttpResponse('<h1>Hola! :)</h1>')