
from pyexpat.errors import messages
from urllib import request
from django.shortcuts import render, redirect 
from django.core.exceptions import ObjectDoesNotExist 
from cv.forms import CVForm 
from .models import CV




def cv_list(request):
    cv_list = CV.objects.all()
    data = {'cv_list': cv_list}
    return render(request, 'cv/cv_list.html', data)

def cv_add(request):
    if request.method == 'POST':
        form = CVForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('cv:cv_list')
    else:
        form = CVForm()
    context = {'form': form}
    return render(request, 'cv/cv_form.html', context)

def cv_edit(request, pk):
    cv = CV.objects.get(pk=pk)
    if request.method == 'POST':
        form = CVForm(request.POST, request.FILES, instance=cv)
        if form.is_valid():
            form.save()
            return redirect('cv:cv_list')
    else:
        form = CVForm(instance=cv)
    context = {'form': form, 'cv': cv}
    return render(request, 'cv/cv_edit.html', context)


def cv_delete(request, pk):
    try:
        cv = CV.objects.get(pk=pk)
        cv.delete()
    except ObjectDoesNotExist:
        message = "CV not found."
        return render(request, 'cv_delete.html', {'error': message})  
    return redirect('cv:cv_list')  # Redirect to CV list view after successful deletion





