from django.shortcuts import render
from goods.models import Product

# Create your views here.


def index(request):
    context = dict()
    goods = Product.objects.all()

    return render(request, 'goods/index.html', {'goods': goods})



