from django.shortcuts import render
from django.utils import timezone
from .models import Post #Kropka przed modelami models oznacza bieżący katalog; nazwę pliku models.py podejemy bez .py

def post_list(request):
    #posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date') #filtrowanie data publikacji postu mniejsza (lte) data bieżąca
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

    
