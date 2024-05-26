from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login
# Create your views here.
def register_view(request):
    if request.method == "POST":
     form = UserCreationForm(request.POST)
     print(request.method)
     print(form.is_valid())
     print(form.fields.values())
     if form.is_valid():
      print(form.is_valid())
      auth_login(request,form.get_user())
      return redirect("posts:list")
    else:
     form = UserCreationForm()

    return render(request, 'users/register.html',  {"form":form})

def login_view(request):
    if request.method == 'POST':
     form = AuthenticationForm(data=request.POST)
     if form.is_valid():
      print(form.is_valid())
      return redirect("posts:list")
    else:
        form = AuthenticationForm()
        
    return render(request,'users/login.html', {"form":form})