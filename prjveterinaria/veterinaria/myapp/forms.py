from django import forms
from django.forms import ModelForm
from .models import Dueños, Animales, AdminUsers

class DueñosForms(ModelForm):
    class Meta:
        model = Dueños
        fields = "__all__"

class AnimalesForms(ModelForm):
    class Meta:
        model = Animales
        fields = "__all__"


""""
class LoginForm(forms.Form):
    username = forms.EmailField(label="Email adress",widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'username', 'name': 'username'}))
    password = forms.CharField(label="Password",widget=forms.PasswordInput (attrs={'class': 'form-control' , 'placeholder': 'password', 'name': 'password'}))
"""

