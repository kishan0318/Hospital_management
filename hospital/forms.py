from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import fields
from django.forms.widgets import Widget
from django.contrib.auth import authenticate


class Register(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    retype_password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=['username',"first_name","last_name","email"]
    def clean(self):
        super().clean()
        p=self.cleaned_data.get('password') 
        p1=self.cleaned_data.get("retype_password")
        self.cleaned_data.get('user_type')
        if p!=p1:
            raise forms.ValidationError("both passwords didn't match")
 
class Logform(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    def clean(self):
        u=self.cleaned_data.get('username')
        p=self.cleaned_data.get('password')
        ur=authenticate(username=u,password=p)
        if ur==None:
            raise forms.ValidationError("user does not exist try again")


