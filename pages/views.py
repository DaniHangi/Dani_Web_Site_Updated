# from django.http import Http404
from urllib import request
from pages.forms import ContactForm
from twomodels.models import *
from django.shortcuts import get_object_or_404, render   # type: ignore
from django.shortcuts import render, redirect
from django.core.mail import  send_mail
from django.template.loader import render_to_string


def home(request):
    return render(request, 'pages/home.html')


def about(request):
    return render(request, 'pages/about.html')

# def services(request):
    
#     developer = get_object_or_404(Developer, name="Dani")
#     return render(request, 'pages/service.html', {'developer': developer})


def services(request):
    
    developer = get_object_or_404(Developer, name="Dani")
    return render(request, 'pages/service.html', {'developer':developer})




# def services(request):
#     developers = Developer.objects.all()  # Get all developers
#     context = {'developers': developers}
#     return render(request, 'services.html', context)  # Use 'services.html' for your template name





def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            content = form.cleaned_data['message']
            time = form.cleaned_data['done_at']
            form.save()  # Save form data to the database
            # Optionally, send a success message or redirect to a confirmation page
            print('The form was valid!')
            html = render_to_string('pages/contactform.html', {  
                'name': name,
                'email': email,
                'content': content,
                'time' : time,
            })
            send_mail('The contact form subject', 'This is the message content','user@gmail.com', ['danihangikasereka9@gmail.com'], html_message=html)
            return redirect ('pages:contact')  # Replace with your redirect URL
    else:
        form = ContactForm()  # Create an empty form for GET requests

    context = {'form': form}
    return render(request, 'pages/contact.html', context)


