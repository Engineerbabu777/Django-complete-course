from django.shortcuts import render,redirect
from .models import Post
from django.contrib.auth.decorators import login_required
from . import forms
# Create your views here.
def posts_lists(request):
    post = Post.objects.all().order_by('-date')
    return render(request, 'posts/post_list.html', {'posts':post})

def post_page(request, slug):
 post = Post.objects.get(slug=slug)
 return render(request, 'posts/post_page.html', {'post':post})

@login_required(login_url="/users/login/")
def  post_new(request):
    if request.method == "POST":
        form = forms.CreatePost(request.POST, request.FILES)   
        if form.is_valid():
            return redirect('posts:list') 
        
    else:
        form = forms.CreatePost()
        
    return render(request, "posts/post_new.html")