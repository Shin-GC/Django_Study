from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index),
    path('hello/', views.hello_view),
    path('menus/<str:food>/', views.food_detail),
]
