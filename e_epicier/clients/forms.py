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
      

    # email = forms.EmailField()
    # email.widget.attrs['class'] = 'form-control'

    # def __init__(self, *args, **kwargs):
        
    #     super().__init__(*args,**kwargs)
    #     self.fields['username'].widget.attrs.update({'class':'form-control'})
    #     self.fields['password1'].widget.attrs.update({'class':'form-control'})
    #     self.fields['password2'].widget.attrs.update({'class':'form-control'})


    # class Meta:
    #     model = User
    #     fields = ['username','email','password1','password2']