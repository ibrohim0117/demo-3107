from django.shortcuts import render

from .models import Post

def home_view(request):
    return render(request, 'home.html')

def post_view(request):
    post_list = Post.objects.all()
    return render(request, 'posts.html', context={'posts': post_list})