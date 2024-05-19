from django import forms
from .models import Developer

class DeveloperForm(forms.ModelForm):
    class Meta:
        model = Developer
        # fields = '__all__'  # Include all fields by default
        # Or, for more granular control:
        fields = ['name', 'biography', 'image', 'email', 'phone_number', 'website_url']

    def clean_email(self):
        """
        Custom validation for the email field.

        Ensures the email is unique (excluding the current object if editing).
        """
        email = self.cleaned_data['email']
        if Developer.objects.filter(email=email).exists():
            current_object = self.instance.pk if self.instance.pk else None
            if current_object is None or email != Developer.objects.get(pk=current_object).email:
                raise forms.ValidationError('This email address is already in use.')
        return email

