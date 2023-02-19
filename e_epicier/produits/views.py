from django.shortcuts import render,redirect
from .forms import ProduitForm
from .models import Produit 
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def produitView(request):
    produits = Produit.objects.filter(user=request.user).values
    return render(request, 'produits/produit_view.html',{'produits':produits})

@login_required
def produitDetail(request,id):
    produit = Produit.objects.get(id=id)
    if check(produit,request): return redirect('home')
    return render(request, 'produits/produit_detail.html',{'produit':produit})

@login_required
def produitEdit(request,id):
    produit = Produit.objects.get(id=id)
    if check(produit,request): return redirect('home')
    if request.method == 'POST':
        form = ProduitForm(request.POST,instance = produit)
        if form.is_valid():
            form.save()
            messages.success(request, "Produit has been Updated")
            return redirect('produit-view')
    else:
        form = ProduitForm(instance = produit)
    return render(request, 'produits/produit_edit.html',{'form':form})

@login_required
def produitAdd(request):
    if request.method == 'POST':
        form = ProduitForm(request.POST)
        if form.is_valid():
            i = form.save(commit=False)
            i.user = request.user
            i.save()
            messages.success(request, "Produit has been added")
            return redirect('produit-view')
    else:
        form = ProduitForm()
    return render(request,'produits/produit_add.html',{'form':form})

@login_required
def produitDelete(request,id):
    produit = Produit.objects.get(id=id)
    if check(produit,request): return redirect('home')
    produit.delete()
    return redirect('produit-view')

def check(model, request):
    if(model.user != request.user):
        messages.error(request, "Can't access this page")
        return True