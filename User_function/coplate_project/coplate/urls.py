from django.urls import path, include
from . import views
from django.contrib import admin

urlpatterns = [
    path('',
         views.IndexView.as_view(),
         name='index'),

    path('reviews/<int:review_id>/',
         views.ReviewDetailView.as_view(),
         name="review-detail"),

    path('reviews/new/', views.ReviewCreateView.as_view(), name="review-create"),
]
