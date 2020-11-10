from django.contrib.auth.models import User
from django.http import request
from django.shortcuts import render
from .models import Post
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView

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



class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    

class PostDetailedView(DetailView):
    model = Post
    template_name = 'blog/detailed.html'


class MyBlogPostListView(ListView):
    model = Post
    template_name = 'blog/myblogs.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    

class MyBlogPostDetailedView(DetailView):
    model = Post
    template_name = 'blog/myblogdetailed.html'



