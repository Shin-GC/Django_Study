from django.shortcuts import render
from datetime import datetime


def index(request):
    today = str(datetime.now().date())
    context = {'date': today}
    return render(request, "menus/index.html", context=context)
