from django.shortcuts import render,redirect
from .forms import ClientForm
from .models import Client
from django.contrib import messages

# Create your views here.

def clientView(request):
    clients = Client.objects.all()
    return render(request, 'clients/client_view.html',{'clients':clients})

def clientDetail(request,id):
    client = Client.objects.get(id=id)
    return render(request, 'clients/client_detail.html',{'client':client})

def clientEdit(request,id):
    client = Client.objects.get(id=id)
    if request.method == 'POST':
        form = ClientForm(request.POST,instance = client)
        if form.is_valid():
            form.save()
            messages.success(request, "Client has been Updated")
            return redirect('client-view')
    else:
        form = ClientForm(instance = client)
    return render(request, 'clients/client_edit.html',{'form':form})

def clientAdd(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Client has been added")
            return redirect('client-view')
    else:
        form = ClientForm()
    return render(request,'clients/client_add.html',{'form':form})

def clientDelete(request,id):
    client = Client.objects.get(id=id)
    client.delete()
    return redirect('client-view')