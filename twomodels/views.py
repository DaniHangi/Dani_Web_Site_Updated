from django.shortcuts import render, get_object_or_404, redirect
from .models import Developer
from .forms import DeveloperForm

def developer_detail(request, dev_id):
    developer = get_object_or_404(Developer, dev_id=dev_id)
    return render(request, 'twomodels/developer_detail.html', {'developer' : developer})



def edit_developer(request, dev_id):
    developer = get_object_or_404(Developer, dev_id=dev_id)

    if request.method == 'POST':
        form = DeveloperForm(request.POST, instance=developer)  # Pass existing object
        if form.is_valid():
            form.save()
            return redirect('twomodels:developer-detail' ,dev_id=developer.pk)  # Redirect to success page
    else:
        form = DeveloperForm(instance=developer)  # Pre-populate with existing data
    context = {'developer': developer, 'form': form}
    return render(request, 'twomodels/edit_developer.html', context)
