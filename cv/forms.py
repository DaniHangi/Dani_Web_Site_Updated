from django import forms 
from .models import CV  # Assuming CV model is in the same app

class CVForm(forms.ModelForm):
    class Meta:
        model = CV
        fields = ['name', 'email', 'skills']
