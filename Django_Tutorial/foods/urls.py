from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('hello/', views.hello_view),
    path('menu/<str:food>/', views.food_detail),
]
