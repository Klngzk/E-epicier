from django.shortcuts import render,redirect,reverse
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
    return render(request,'users/regi_log.html',{'form':form})
# login page
def loginpage(request):
    username = request.POST.get('username2')
    password = request.POST.get('password')
    user = authenticate(request,username=username,password=password)
    if user is not None:
        login(request,user)
        return redirect('home')
    else:
        messages.error(request, "Problem")
    return render(request,'users/regi_log.html')

def authenticatePage(request):
    if request.user.is_authenticated:
        messages.info(request,"You are already athenticated")
        return redirect('home')
    if request.method == 'POST' and 'username2' in request.POST:
        return loginpage(request)
    elif request.method == 'POST':
        print(request.POST)
        return register(request)
    else:
        form = UserRegisterform()
    return render(request,'users/regi_log.html',{'form':form})

# logout 
def logoutpage(request):
    logout(request)
    return redirect('login')
#pages
def aboutUs(request):
    return redirect('/#about')
def services(request):
    return redirect('/#service')
def contact_us(request):
    return redirect('/#contact')
@login_required
def manage(request):
    return render(request,'manage.html')

  
