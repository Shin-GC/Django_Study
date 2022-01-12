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


class PostCreateView(CreateView):
    model = Post
    template_name = "podomarket/post_form.html"
    form_class = PostCreateForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
        # 유효성 검증에 통과 한다면 super()를 통해 Form class에 사용자를 넣어준 후 넘겨준다.

    def get_success_url(self):
        return reverse("post-detail", kwargs={"post_id": self.object.id})


class PostDeleteView(DeleteView):
    model = Post
    template_name = "podomarket/post_confirm_delete.html"
    pk_url_kwarg = "post_id"

    def get_success_url(self):
        return reverse("index")


class PostUpdateView(UpdateView):
    model = Post
    template_name = "podomarket/post_form.html"
    form_class = PostUpdateForm
    pk_url_kwarg = "post_id"

    def get_success_url(self):
        return reverse("post-detail", kwargs={"post_id": self.object.id})
