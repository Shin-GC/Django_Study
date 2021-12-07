from django.shortcuts import render
<<<<<<< Updated upstream
from django.http import HttpResponse
from django.http import Http404
=======
from django.http import Http404
from datetime import datetime
from foods.models import Menu

>>>>>>> Stashed changes
# Create your views here.


def index(request):
<<<<<<< Updated upstream
    return render(request, "foods/index.html")

=======
    context = {}
    today = str(datetime.today().date())
    menus = Menu.objects.all()
    context['date'] = today
    context['menus'] = menus
>>>>>>> Stashed changes

    return render(request, 'foods/index.html', context=context)


<<<<<<< Updated upstream
def food_detail(request, food):
    context = dict()

    if food == 'chicken':
        context['name'] = '코딩에 빠진 닭'
        context['description'] = '주머니가 가벼운 당신의 마음까지 생각한 가격!'
        context['price'] = 19000
        context['img_path'] = 'foods/images/chicken.jpg'
    else:
        raise Http404('이런 음식은 판매하지 않습니다.')

=======
def food_detail(request, pk):
    context = dict()
    menu = Menu.objects.get(id=pk)
    context['menu'] = menu
>>>>>>> Stashed changes
    return render(request, 'foods/detail.html', context=context)
