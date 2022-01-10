from django.shortcuts import render
from django.urls import reverse
from allauth.account.views import PasswordChangeView, PasswordResetView
from django.views.generic import ListView, DetailView
from coplate.models import Review, User


class CustomPasswordChangeView(PasswordChangeView):
    def get_success_url(self):  # 어떠한 폼이 성공적으로 처리되면 어디로 리디렉션 될지 정해주는 함수
        return reverse("index")


class CustomPasswordResetView(PasswordResetView):
    def get_success_url(self):
        return reverse("index")


class IndexView(ListView):
    model = Review
    template_name = "coplate/index.html"
    context_object_name = "reviews"
    paginate_by = 4
    ordering = ["-dt_created"]


class ReviewDetailView(DetailView):
    model = Review
    template_name = "coplate/review_detail.html"
    pk_url_kwarg = "review_id"
