from django.shortcuts import render
from .models import Post


def all_blogs(request):
    posts = Post.objects.order_by('-date')

    return render(request, 'all_blogs.html', {'posts': posts})
