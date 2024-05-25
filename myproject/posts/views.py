from django.shortcuts import render
from .models import Post
# Create your views here.
def posts_lists(request):
    post = Post.objects.all().order_by('-date')
    return render(request, 'posts/post_list.html', {'posts':post})

