from django import forms
from .models import Qnt_Produit, Credit
from produits.models import Produit
from clients.models import Client

# class Produit_QntForm(forms.ModelForm):
#     class Meta:
#         model = Qnt_Produit
#         fields = ['produit', 'qnt']
#         widgets = {
#             'produit': forms.Select(attrs={'class': 'form-control'}),
#             'qnt': forms.NumberInput(attrs={'class': 'form-control'}),
#         }

class CreditForm(forms.ModelForm):
    class Meta:
        model = Credit
        fields = ['titre','client','to_pay','payed']
        widgets = {
            'client': forms.Select(attrs={'class': 'form-control'}),
            'titre': forms.TextInput(attrs={'class': 'form-control'}),
            'to_pay': forms.TextInput(attrs={'class': 'form-control','readonly': True}),
            'payed': forms.TextInput(attrs={'class': 'form-control','readonly': True}),
            
        }

class SelectedProductForm(forms.ModelForm):
    class Meta:
        model = Qnt_Produit
        fields = ['produit', 'credit','qnt','total']
        widgets = {
            'total': forms.NumberInput(attrs={'class': 'total'}),
        }