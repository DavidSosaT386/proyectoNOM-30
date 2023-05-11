from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import anexos, porfile
class CustomUserCreationForm(UserCreationForm):
    pass

class anexosForm(forms.ModelForm):
    class Meta:
        model = anexos
        exclude = ['no_reporte']

class perfilForm(forms.ModelForm):
    class Meta:
        model =  porfile
        fields = ['foto_perfil'] 
        
      
 