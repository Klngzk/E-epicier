from django import forms
from django.forms import ModelForm
from .models import Produit

class ProduitForm(ModelForm):
    class Meta:
        model = Produit
        fields = ['name','prix']
        widgets={
            'name' : forms.TextInput(attrs={'onkeyup':'this.setAttribute("value", this.value);','value':""}),
            'prix' : forms.NumberInput(attrs={'onkeyup':'this.setAttribute("value", this.value);','value':"",'min':'0'}),
        }
