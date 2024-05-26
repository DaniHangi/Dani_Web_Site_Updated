
from pyexpat.errors import messages
# from urllib import request
from django.shortcuts import render, redirect 
from django.core.exceptions import ObjectDoesNotExist 
import cv
from cv.forms import CVForm 
from .models import CV
from django.contrib.auth.decorators import login_required, permission_required

# Import Pagination Stuff
from django.core.paginator import Paginator


# @permission_required('cv.delete_cv', raise_exception=True)
# def cv_list(request):
#     cv_list = CV.objects.all()

#     #set up pangination
#     p = Paginator(cv_list, 1)
#     page = request.GET.get('page')
#     cvs_pagination = p.get_page(page)
#     return render(request, 'cv/cv_list.html', {'cv_list': cv_list, 'cvs_pagination': cvs_pagination})

@permission_required('cv.delete_cv', raise_exception=True)
def cv_list(request):
    """
    Renders a paginated list of CVs with search functionality.

    - Handles both search and pagination scenarios.
    - Uses efficient filtering with `icontains` for case-insensitive search.
    - Preserves pagination behavior during searches (optional).
    - Provides clear context for better understanding.
    """

    search_query = request.GET.get('q', '')  # Get search query or set to empty string

    if search_query:
        cv_list = CV.objects.filter(Q(name__icontains=search_query) | Q(summary__icontains=search_query)) # type: ignore
    else:
        cv_list = CV.objects.all()  # Retrieve all CVs if no search query

    # Set up pagination
    p = Paginator(cv_list, 1)  # Adjust page size as needed
    page = request.GET.get('page')
    cvs_pagination = p.get_page(page)

    context = {
        'cvs_pagination': cvs_pagination,
        'search_query': search_query,  # Pass search query for template usage
    }

    return render(request, 'cv/cv_list.html', context)


 
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


@login_required
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