from django import forms
from django.forms import ModelForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Client



class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ['firstname','lastname','numero','cin']
        widgets={
            'firstname' : forms.TextInput(attrs={'onkeyup':'this.setAttribute("value", this.value);','value':""}),
            'lastname' : forms.TextInput(attrs={'onkeyup':'this.setAttribute("value", this.value);','value':""}),
            'numero' : forms.TextInput(attrs={'onkeyup':'this.setAttribute("value", this.value);','value':""}),
            'cin' : forms.TextInput(attrs={'onkeyup':'this.setAttribute("value", this.value);','value':""}),
        }