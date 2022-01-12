from django.urls import path, include
from . import views

urlpatterns = [
    path('',
         views.IndexView.as_view(),
         name='index'),

    path('post/<int:post_id>/',
         views.PostDetailView.as_view(),
         name="post-detail"),

    path('post/new/',
         views.PostCreateView.as_view(),
         name='post-create'),

    path('post/<int:post_id>/delete/',
         views.PostDeleteView.as_view(),
         name="post-delete"),

    path('post/<int:post_id>/edit/',
         views.PostUpdateView.as_view(),
         name="post-update"),
]
