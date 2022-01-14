from django.shortcuts import render
from allauth.account.views import PasswordChangeView
from django.urls import reverse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    DeleteView,
    UpdateView
)

from podomarket.models import Post
from podomarket.forms import PostUpdateForm, PostCreateForm
from braces.views import LoginRequiredMixin, UserPassesTestMixin
from allauth.account.models import EmailAddress
from podomarket.functions import confirmation_required_redirect


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


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = "podomarket/post_detail.html"
    pk_url_kwarg = "post_id"


class PostCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Post
    template_name = "podomarket/post_form.html"
    form_class = PostCreateForm

    redirect_unauthenticated_users = True
    raise_exception = confirmation_required_redirect

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
        # 유효성 검증에 통과 한다면 super()를 통해 Form class에 사용자를 넣어준 후 넘겨준다.

    def get_success_url(self):
        return reverse("post-detail", kwargs={"post_id": self.object.id})

    def test_func(self, user):
        return EmailAddress.objects.filter(user=user, verified=True).exists()


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "podomarket/post_confirm_delete.html"
    pk_url_kwarg = "post_id"

    raise_exception = True

    def get_success_url(self):
        return reverse("index")

    def test_func(self, user):
        post = self.get_object()
        return post.author == user


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = "podomarket/post_form.html"
    form_class = PostUpdateForm
    pk_url_kwarg = "post_id"

    raise_exception = True

    def get_success_url(self):
        return reverse("post-detail", kwargs={"post_id": self.object.id})

    def test_func(self, user):
        post = self.get_object()
        return post.author == user
