from django.shortcuts import render
from .models import Post

def all_blogs(request):
    blogs = Post.objects.all()
    return render(request, 'blog/all_blogs.html', {'blogs':blogs})