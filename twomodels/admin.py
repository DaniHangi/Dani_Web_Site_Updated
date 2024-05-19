from django.contrib import admin  # type: ignore

# import the models
from .models import *

# register each model with the admin site
admin.site.register(Developer)
admin.site.register(ContactRequest)