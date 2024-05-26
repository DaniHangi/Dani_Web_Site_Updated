# pages/urls.py


from django.urls import path  # type: ignore
from . import views


app_name = 'pages'
urlpatterns = [
    # Standalone Web Pages

    path('', views.home, name='home'),
    path('about-me/', views.about, name='about'),
    path('my-services/', views.services, name='services'),
    path('my-contact/', views.contact_view, name='contact'),
  
]
