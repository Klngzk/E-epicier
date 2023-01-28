from django import forms
from django.forms import ModelForm
from .models import Produit

class ProduitForm(ModelForm):
    class Meta:
        model = Produit
        fields = ['name','prix']
        widgets={
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'prix' : forms.TextInput(attrs={'class':'form-control'}),
        }
