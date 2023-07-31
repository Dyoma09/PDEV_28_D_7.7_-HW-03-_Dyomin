from datetime import datetime

from django.urls import reverse_lazy

from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Author
from .filters import NewsFilter
from .forms import NewsForm

class AuthorList(ListView):
    model = Author
    context_object_name = 'Author'

class ListNews(ListView):
    model = Post
    ordering = 'post_title'
    template_name = 'news_test.html'
    context_object_name = 'news_list'
   
    queryset = Post.objects.filter(post_type='NW').order_by('-id')

    paginate_by = 10

   #  def get_queryset(self):
       
   #     queryset = super().get_queryset()
   #     self.filterset = NewsFilter(self.request.GET, queryset)
   #     return self.filterset.qs
    
   #  def get_context_data(self, **kwargs):
   #    context = super().get_context_data(**kwargs)
   #    context['filterset'] = self.filterset
   #    return context
    
class ListNewsSearch(ListView):
    model = Post
    ordering = 'post_title'
    template_name = 'news_search_test.html'
    context_object_name = 'news_search'

    paginate_by = 5

    def get_queryset(self):
       
        queryset = super().get_queryset()
        self.filterset = NewsFilter(self.request.GET, queryset)
        return self.filterset.qs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context
    
class DetailNews(DetailView):
    model = Post
    template_name = 'news_detail.html'
    context_object_name = 'news'


class CreateNews(CreateView):
    form_class = NewsForm
    model = Post
    template_name = 'news_create.html'
    success_url = reverse_lazy('news')

    def form_valid(self, form):
        post = form.save(commit=False)
        post.post_type = 'NW'
        return super().form_valid(form)


class UpdateNews(UpdateView):
    form_class = NewsForm
    model = Post
    template_name = 'news_create.html'
    success_url = reverse_lazy('news')


class DeleteNews(DeleteView):
    model = Post
    template_name = 'news_delete.html'
    success_url = reverse_lazy('news')


class ArticleCreate(CreateView):
    form_class = NewsForm
    model = Post
    template_name = 'article_create.html'
    success_url = reverse_lazy('news')

    def form_valid(self, form):
        post = form.save(commit=False)
        post.post_type = 'AT'
        return super().form_valid(form)


class ArticleUpdate(UpdateView):
    form_class = NewsForm
    model = Post
    template_name = 'article_create.html'
    success_url = reverse_lazy('news')


class ArticleDelete(DeleteView):
    model = Post
    template_name = 'news_delete.html'
    success_url = reverse_lazy('news')
    
