from django.urls import path
from .views import PostListView, PostDetailedView, MyBlogPostListView, MyBlogPostDetailedView
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailedView.as_view(), name='blog-detailed'),
    path('about/', views.about, name='blog-about'),
    path('myblogs/', MyBlogPostListView.as_view(), name='my-blogs'),
    path('mypost/<int:pk>/', MyBlogPostDetailedView.as_view(), name='myblog-detailed'),

]
