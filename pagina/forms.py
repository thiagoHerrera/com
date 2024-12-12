from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core import validators
from .models import Food

class CustomTextInput(forms.TextInput):
    def _init_(self, *args, **kwargs):
        kwargs

class RegisterForm(UserCreationForm):
    
        username = forms.CharField()
        email = forms.EmailField()
        password1 = forms.CharField()
        password2 = forms.CharField()
        class Meta:
            model = User
            fields = ['username','email','password1','password2']
        
from .models import Suplemento

class SuplementoForm(forms.ModelForm):
    class Meta:
        model = Suplemento
        fields = ['nombre', 'descripcion', 'imagen']

class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ['name', 'calories', 'grams'] 