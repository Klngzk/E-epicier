from django.shortcuts import render,redirect
from .forms import  CreditForm,SelectedProductForm
from .models import Credit,Qnt_Produit
from .models import Produit
from django.contrib import messages

import decimal
# Create your views here.


def creditAdd(request):
    if request.method == 'POST':
        form = CreditForm(request.POST)
        if form.is_valid():
            i = form.save(commit=False)
            i.user = request.user
            i.to_pay=0.00
            i.payed =0.00
            i.save()
            id_credit = i.id 
            return redirect('credit-produit', id= id_credit)
    else:
        form = CreditForm()
    return render(request,'credits/credit_add.html',{'form':form})

def creditEdit(request,id):
    credit = Credit.objects.get(id=id)
    produits = Qnt_Produit.objects.filter(credit=id)
    if request.method == 'POST' and 'pay' in request.POST:
        creditPay(request,id)
        credit = Credit.objects.get(id=id)
        form = CreditForm(instance = credit)
    elif request.method == 'POST':
        form = CreditForm(request.POST,instance = credit)
        if form.is_valid():
            form.save()
            # messages.success(request, "Client has been Updated")
            return redirect('credit-view')
    else:
        form = CreditForm(instance = credit)
    return render(request,'credits/credit_edit.html',{'form':form,'produits':produits, 'id':id})


def creditDetail(request):
    credits = Credit.objects.filter(user=request.user)


def creditDelete(request,id):
    credit = Credit.objects.get(id=id)
    credit.delete()
    return redirect('credit-view')

def creditProduits(request,id):
    produits = Produit.objects.filter(user=request.user).values
    credit = Credit.objects.get(id=id)
    total =0
    if request.method == 'POST':
        for product in Produit.objects.all():
            quantity = int(request.POST.get(f'quantity_{product.id}', 0))
            if quantity > 0:
                total += quantity*product.prix
                selected_product = Qnt_Produit(produit=product, qnt=quantity, credit = credit,total=quantity*product.prix)
                selected_product.save()
        credit.to_pay +=total
        credit.save()
        return creditView(request)
    return render(request,'produits/produit_credit_add.html',{'produits':produits})


def creditPay(request,id):
    credit = Credit.objects.get(id=id)
    pay = decimal.Decimal(request.POST.get('pay'))
    to_pay = credit.to_pay
    if(pay > to_pay):
        return messages.error(request,"You are paying more than you need")
    to_pay -= pay
    credit.to_pay = to_pay
    credit.payed += pay
    credit.save()
    return messages.success(request,"Good")

def creditView(request):
    credits = Credit.objects.filter(user=request.user)
    return render(request, 'credits/credit_view.html',{'credits':credits})