from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *
from .filters import PostFilter, PostFilter2
from .forms import *
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect


class News(ListView):
    model = Post
    # ordering = '-time_in'
    # queryset = Post.objects.order_by('-time_in')
    queryset = Post.objects.filter(Wahl='Nachricht')
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = 2

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     self.filterset = PostFilter(self.request.GET, queryset)
    #     return self.filterset.qs
    #
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['filterset'] = self.filterset
    #     return context


class Articles(ListView):
    model = Post
    # ordering = '-time_in'
    # queryset = Post.objects.order_by('-time_in')
    queryset = Post.objects.filter(Wahl='Artikel')
    template_name = 'articles.html'
    context_object_name = 'articles'
    paginate_by = 2


class Search(ListView):
    model = Post
    queryset = Post.objects.order_by('-time_in')
    template_name = 'search.html'
    context_object_name = 'search'

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     self.filterset = PostFilter(self.request.GET, queryset)
    #     return self.filterset.qs
    #
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['filterset'] = self.filterset
    #     return context

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter2(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class New(DetailView):
    model = Post
    queryset = Post.objects.filter(Wahl='Nachricht')
    template_name = 'new.html'
    context_object_name = 'new'


class Article(DetailView):
    model = Post
    queryset = Post.objects.filter(Wahl='Artikel')
    template_name = 'article.html'
    context_object_name = 'article'


class PostCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'

    def form_valid(self, form):
        new = form.save(commit=False)
        new.Wahl = 'Nachricht'
        return super().form_valid(form)


class ArticleCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'article_edit.html'

    def form_valid(self, form):
        article = form.save(commit=False)
        article.Wahl = 'Artikel'
        return super().form_valid(form)


class PostUpdate(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'


class ArticleUpdate(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'article_edit.html'


class PostDelete(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('news')


class ArticleDelete(DeleteView):
    model = Post
    template_name = 'article_delete.html'
    success_url = reverse_lazy('articles')


# def create_post(request):
#     form = PostForm()
#     if request.method == 'POST':
#         form = PostForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/news/')
#     return render(request, 'post_edit.html', {'form': form})
# Create your views here.
