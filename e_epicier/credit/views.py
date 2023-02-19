from django.shortcuts import render,redirect
from .forms import  CreditForm,SelectedProductForm
from .models import Credit,Qnt_Produit
from .models import Produit
from django.contrib import messages
from django.contrib.auth.decorators import login_required

import decimal
# Create your views here.

@login_required
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

@login_required
def creditEdit(request,id):
    credit = Credit.objects.get(id=id)
    if check(credit,request): return redirect('home')
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
    return render(request,'credits/credit_edit.html',{'form':form,'produits':produits, 'id':id,'credit':credit})

def creditDetail(request,id):
    credits = Credit.objects.get(id=id)
    produits = Qnt_Produit.objects.filter(credit=id)
    return render(request, 'credits/credit_detail.html',{'credits':credits,'produits':produits})

@login_required
def creditDelete(request,id):
    credit = Credit.objects.get(id=id)
    if check(credit,request): return redirect('home')
    credit.delete()
    return redirect('credit-view')

@login_required
def creditProduits(request,id):
    produits = Produit.objects.filter(user=request.user).values
    credit = Credit.objects.get(id=id)
    if check(credit,request): return redirect('home')
    total =0
    if request.method == 'POST':
        for product in Produit.objects.all():
            quantity = int(request.POST.get(f'quantity_{product.id}', 0))
            if quantity > 0:
                total += quantity*product.prix
                selected_product = Qnt_Produit(produit=product, qnt=quantity, credit = credit,total=quantity*product.prix)
                selected_product.save()
        credit.to_pay +=total
        credit.etat = 0
        credit.save()
        return creditView(request)
    return render(request,'produits/produit_credit_add.html',{'produits':produits})

@login_required
def creditPay(request,id):
    credit = Credit.objects.get(id=id)
    if check(credit,request): return redirect('home')
    pay = decimal.Decimal(request.POST.get('pay'))
    to_pay = credit.to_pay
    if(pay > to_pay):
        return messages.error(request,"You are paying more than you need")
    to_pay -= pay
    credit.to_pay = to_pay
    credit.payed += pay
    
    if(credit.to_pay == 0.00): 
        credit.etat = 1
    else:
        credit.etat = 0
    credit.save()
    return messages.success(request,"Good")

@login_required
def creditView(request):
    credits = Credit.objects.filter(user=request.user)
    return render(request, 'credits/credit_view.html',{'credits':credits})

def creditCheck(request):
    if request.method == 'POST':
        credit_id = request.POST.get('credit_id')
        try:
            credit = Credit.objects.get(id=credit_id)
            return redirect('credit-detail', id=credit.id)
        except Credit.DoesNotExist:
            messages.error(request, 'Credit not found')
        except ValueError:
             messages.error(request, 'Invalid Value')

    return render(request, 'credits/credit_find.html')


def check(model, request):
    if(model.user != request.user):
        messages.error(request, "Can't access this page")
        return True