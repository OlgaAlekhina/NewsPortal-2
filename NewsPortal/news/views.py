from django.shortcuts import render
from django.views import View
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .filters import PostFilter
from .forms import PostForm


class NewsList(ListView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'news'
    ordering = ['-post_time']
    paginate_by = 10


class NewsDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'

class NewsSearch(ListView):
    model = Post
    template_name = 'search.html'
    context_object_name = 'news'
    ordering = ['-post_time']
    paginate_by = 2
    queryset = Post.objects.order_by("pk")

    def get_filter(self):
        return PostFilter(self.request.GET, queryset=super().get_queryset())

    def get_queryset(self):
        qs = self.get_filter().qs
        return qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        filter = self.get_filter()
        context['filter'] = filter

        filter_params = ""
        for f_name in [str(k) for k in filter.filters]:
            if f_name in filter.data:
                filter_params += f"&{f_name}={filter.data[f_name]}"
        context['filter_params'] = filter_params

        context['get_dict'] = {
            k: value[0] for k, value in dict(self.request.GET.copy()).items() if k != 'page'
         }
        return context


class NewsCreateView(CreateView):
    template_name = 'post_create_form.html'
    form_class = PostForm

class NewsUpdateView(UpdateView):
    template_name = 'post_update_form.html'
    form_class = PostForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)

class NewsDeleteView(DeleteView):
    template_name = 'post_delete_form.html'
    queryset = Post.objects.all()
    success_url = '/news/'



