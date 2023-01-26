from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate , login ,logout

from .forms import UserRegisterform
# home page
def home(request):
    # open home page
    return render(request,'home.html')
# register page
def register(request):
    # if user is logged in redirect to home page
    if request.user.is_authenticated:
        messages.info(request,"You are already athenticated")
        return redirect('home')
    # register logic
    if request.method == 'POST':
        form = UserRegisterform(request.POST)
        # is user infos are valid
        if form.is_valid():
            form.save()
            messages.success(request, "Account is created, Try Logging")
            return redirect('login')
    else:
        form = UserRegisterform()
    return render(request,'users/register.html',{'form':form})
# login page
def loginpage(request):
    if request.user.is_authenticated:
        messages.info(request,"You are already athenticated")
        return redirect('home')
    # login logic
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request, "Problem")
    return render(request,'users/login.html')
# logout 
def logoutpage(request):
    logout(request)
    return redirect('login')