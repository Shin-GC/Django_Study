from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.views.generic import (
    CreateView, ListView, DetailView, UpdateView, DeleteView, RedirectView
)
from django.urls import reverse
from .models import Page
from .forms import PageForm


class PageListView(ListView):
    model = Page
    template_name = 'diary/page_list.html'
    context_object_name = 'diary'
    ordering = ['-dt_created']
    paginate_by = 6
    page_kwarg = 'page'


class PageDetailView(DetailView):
    model = Page
    template_name = 'diary/page_detail.html'
    pk_url_kwarg = 'page_id'
    context_object_name = 'page'


class IndexRedirectView(RedirectView):
    pattern_name = 'post-list'


# def info(request):
#     return render(request, 'diary/info.html')


class PageCreateView(CreateView):
    model = Page
    form_class = PageForm
    template_name = 'diary/page_form.html'

    def get_success_url(self):
        return reverse('page-detail', kwargs={'page_id': self.object.id})


class PageDeleteView(DeleteView):
    model = Page
    template_name = 'diary/page_confirm_delete.html'
    pk_url_kwarg = 'page_id'
    context_object_name = 'page'

    def get_success_url(self):
        return reverse('page-list')


# def page_delete(request, page_id):
#     page = Page.objects.get(id=page_id)
#     if request.method == 'POST':
#         page.delete()
#         return redirect('page-list')
#     else:
#         return render(request, 'diary/page_confirm_delete.html', {'page': page})


class PageUpdateView(UpdateView):
    model = Page
    form_class = PageForm
    pk_url_kwarg = 'page_id'

    def get_success_url(self):
        return reverse('page-detail', kwargs={'page_id': self.object.id})


def index(request):
    return render(request, 'diary/index.html')

# def page_update(request, page_id):
#     page = Page.objects.get(id=page_id)
#
#     if request.method == 'POST':
#         page_form = PageForm(request.POST, instance=page)
#         if page_form.is_valid():
#             page_form.save()
#             return redirect('page-detail', page_id=page.id)
#     else:
#         page_form = PageForm(instance=page)
#     return render(request, 'diary/page_form.html', {'form': page_form})


# def page_create(request):
#     if request.method == 'POST':
#         page_form = PageForm(request.POST)
#         if page_form.is_valid():
#             new_page = page_form.save()
#             return redirect('page-detail', page_id=new_page.id)
#     else:
#         page_form = PageForm()
#     return render(request, 'diary/page_create.html', {'form': page_form})

# class PostCreateView(View):
#
#     def get(self, request):
#         page_form = PageForm()
#         return render(request, 'diary/page_create.html', {'form': page_form})
#
#     def post(self, request):
#         page_form = PageForm(request.POST)
#         if page_form.is_valid():
#             new_page = page_form.save()
#             return redirect('page-detail', page_id=new_page.id)
#         return render(request, 'diary/page_create.html', {'form': page_form})
# Create your views here.

# def page_list(request):
#     pages_list = Page.objects.all()
#     paginator = Paginator(pages_list, 8)
#     curr_page_number = request.GET.get('page')
#
#     if curr_page_number is None:
#         curr_page_number = 1
#
#     page = paginator.page(curr_page_number)
#
#     return render(request, 'diary/page_list.html', {'page': page})
# def page_detail(request, page_id):
#     page = Page.objects.get(id=page_id)
#     context = {'object': page}
#     return render(request, 'diary/page_detail.html', context=context)
