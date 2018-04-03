from django.shortcuts import render, get_object_or_404
from .models import Blog

def allblogs(request):
    blog = Blog.objects
    return render(request, 'blog/allblogs.html', {'blogs': blog})

def detail(request, blog_id):
    detail_blog = get_object_or_404(Blog,pk=blog_id)
    print(detail_blog)
    return render(request, 'blog/detail.html', {'blog': detail_blog})