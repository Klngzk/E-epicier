from django.shortcuts import render,redirect
from .forms import ProduitForm
from .models import Produit 
from django.contrib import messages

# Create your views here.

def produitView(request):
    produits = Produit.objects.all()
    return render(request, 'produits/produit_view.html',{'produits':produits})

def produitDetail(request,id):
    produit = Produit.objects.get(id=id)
    return render(request, 'produits/produit_detail.html',{'produit':produit})

def produitEdit(request,id):
    produit = Produit.objects.get(id=id)
    if request.method == 'POST':
        form = ProduitForm(request.POST,instance = produit)
        if form.is_valid():
            form.save()
            messages.success(request, "Produit has been Updated")
            return redirect('produit-view')
    else:
        form = ProduitForm(instance = produit)
    return render(request, 'produits/produit_edit.html',{'form':form})

def produitAdd(request):
    if request.method == 'POST':
        form = ProduitForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Produit has been added")
            return redirect('produit-view')
    else:
        form = ProduitForm()
    return render(request,'produits/produit_add.html',{'form':form})

def produitDelete(request,id):
    produit = Produit.objects.get(id=id)
    produit.delete()
    return redirect('produit-view')