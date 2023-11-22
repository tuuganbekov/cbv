from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView

from blog.models import Post

def index(request):
    n = 500
    wallet = Post.objects.get(id=1)
    wallet.amount = wallet.amount - n
    wallet.save()
    return render(request, 'index.html', locals())


class PostListView(ListView):
    model = Post
    template_name = 'posts.html'
    context_object_name = 'posts'


class PostDetailView(DetailView):
    model = Post
    template_name = 'post-detail.html'
    context_object_name = 'post'


class PostUpdateView(UpdateView):
    model = Post
    template_name = "post-update.html"
    fields = ["title", "body",]
    success_url = reverse_lazy("posts")


class PostDeleteView(DeleteView):
    model = Post
    template_name = "post-delete.html"
    success_url = reverse_lazy("posts")


class PostCreateView(CreateView):
    model = Post
    template_name = "post-create.html"
    fields = ["title", "body",]
    success_url = reverse_lazy("posts")