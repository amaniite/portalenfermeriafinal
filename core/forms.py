from django import forms
from django.forms import ModelForm
from .models import Profesional
from django.core.validators import RegexValidator
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomEnfermeraForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username','email','password1', 'password2']
        
class ProfesionalForm(forms.ModelForm):
    
    class Meta:
        model = Profesional
        fields = '__all__'
