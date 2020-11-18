from django.contrib.auth.models import User
from django.http import request
from django.shortcuts import render
from django.views.generic.edit import UpdateView
from .models import Post
from django.contrib.auth.decorators import login_required
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView
    )
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# @login_required
# def home(request):
#     context = {
#         'posts': Post.objects.all()
#     }
#     return render(request, 'blog/home.html', context)


# @login_required
# def myBlogs(request):
#     context = {
#         'posts': Post.objects.filter(author=request.user.id)
#     }
#     return render(request, 'blog/myblogs.html',context)


@login_required
def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})



class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    

class PostDetailedView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'blog/detailed.html'


class PostCreateView(LoginRequiredMixin ,CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin ,UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()

        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()

        if self.request.user == post.author:
            return True
        return False



