from django import forms
from django.forms import ModelForm

from rbac import models

class User(ModelForm):
    class Meta:
        model=models.UserInfo
        exclude=['email','roles']
        widgets={
            'password':forms.PasswordInput()
        }