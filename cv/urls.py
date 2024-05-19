from django.urls import path # type: ignore
from . import views

app_name = 'cv'
urlpatterns = [
    path('', views.cv_list, name='cv_list'),
    path('add/', views.cv_add, name='add_cv'),
    path('<int:pk>/edit/', views.cv_edit, name='edit_cv'),
    path('<int:pk>/delete/', views.cv_delete, name='delete_cv'),
   
]
