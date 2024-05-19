from django.urls import path
from . import views  # Assuming your views.py is in the same app


app_name = 'twomodels'
urlpatterns = [
    # path('developers/<int:dev_id>/', views.developer_detail, name='developer-detail'),
    # Other URL patterns
    path('developers/<int:dev_id>/', views.developer_detail, name='developer-detail'),  # Use 'developer-detail' name
    path('developers/<int:dev_id>/edit/', views.edit_developer, name='edit-developer'),
]


