from django import forms 
from .models import CV  # Assuming CV model is in the same app

class CVForm(forms.ModelForm):
    class Meta:
        model = CV
        fields = ['name', 'email', 'skills', 'summary','phone_number', 'portfolio_link', 'cv_file' ]
