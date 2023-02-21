from django.shortcuts import render,redirect
from .forms import ClientForm
from .models import Client
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
@login_required
def clientView(request):
    clients = Client.objects.filter(user=request.user)
    return render(request, 'clients/client_view.html',{'clients':clients})

@login_required
def clientDetail(request,id):
    client = Client.objects.get(id=id)
    if check(client,request): return redirect('home')
    return render(request, 'clients/client_detail.html',{'client':client})

@login_required
def clientEdit(request,id):
    client = Client.objects.get(id=id)
    if check(client,request): return redirect('home')
    if request.method == 'POST':
        form = ClientForm(request.POST,instance = client)
        if form.is_valid():
            i = form.save(commit=False)
            try:
                value = int(i.numero)
            except ValueError:
                messages.error(request, "Invalid Number")
                return render(request,'clients/client_edit.html',{'form':form})
            i.save()
            messages.success(request, "Client has been Updated")
            return redirect('client-view')
    else:
        form = ClientForm(instance = client)
    return render(request, 'clients/client_edit.html',{'form':form})

@login_required
def clientAdd(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            i = form.save(commit=False)
            try:
                value = int(i.numero)
            except ValueError:
                messages.error(request, "Invalid Number")
                return render(request,'clients/client_add.html',{'form':form})
            i.user = request.user
            i.save()
            messages.success(request, "Client has been added")
            return redirect('client-view')
    else:
        form = ClientForm()
    return render(request,'clients/client_add.html',{'form':form})

@login_required
def clientDelete(request,id):
    client = Client.objects.get(id=id)
    if check(client,request): return redirect('home')
    client.delete()
    return redirect('client-view')

def check(model, request):
    if(model.user != request.user):
        messages.error(request, "Can't access this page")
        return True