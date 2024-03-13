from django import forms
from django.forms import ModelForm
from .models import Dueños, Animales, AdminUsers, TurnosClientes

class DueñosForms(ModelForm):
    class Meta:
        model = Dueños
        fields = "__all__"

class AnimalesForms(ModelForm):
    class Meta:
        model = Animales
        fields = "__all__"



class TurneroForms(ModelForm):
    class Meta:
        model = TurnosClientes
        fields = "__all__"