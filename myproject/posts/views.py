from django.shortcuts import render
from .models import Post

# Create your views here.
def posts_lists(request):
    post = Post.objects.all().order_by('-date')
    return render(request, 'posts/post_list.html', {'posts':post})

def post_page(request, slug):
 post = Post.objects.get(slug=slug)
 return render(request, 'posts/post_page.html', {'post':post})

