from django.shortcuts import render
from allauth.account.views import PasswordChangeView
from django.urls import reverse
from django.views.generic import ListView, DetailView
from podomarket.models import Post


# Create your views here.
class IndexView(ListView):
    model = Post
    template_name = "podomarket/index.html"
    context_object_name = "posts"
    paginate_by = 8
    ordering = ["-dt_updated"]


class CustomPasswordChangeView(PasswordChangeView):
    def get_success_url(self):
        return reverse("index")


class PostDetailView(DetailView):
    model = Post
    template_name = "podomarket/post_detail.html"
    pk_url_kwarg = "post_id"
