from django import forms
from models import *
class UserForm(forms.ModelForm):
    class Meta:
        model = Register
        widgets = {
        'password1': forms.PasswordInput(),
        'password2': forms.PasswordInput(),