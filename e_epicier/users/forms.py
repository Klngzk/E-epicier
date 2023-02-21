from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterform(UserCreationForm):
    # add email input
    email = forms.EmailField()
    # add class to input email
    email.widget.attrs['class'] = 'form-style'
    email.widget.attrs['placeholder'] = 'Your Email'
    email.widget.attrs['autocomplete'] = 'off'
    # add classes to the default inputs
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.fields['username'].widget.attrs.update({'class':'form-style','placeholder':'Your Username','autocomplete':'off'})
        self.fields['password1'].widget.attrs.update({'class':'form-style','placeholder':'Your Password','autocomplete':'off'})
        self.fields['password2'].widget.attrs.update({'class':'form-style','placeholder':'Your Password Again'})
    
    class Meta:
        model = User
        fields = ['username','email','password1','password2']