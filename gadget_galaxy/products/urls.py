# products/urls.py
from django.urls import path
from . import views  # Make sure this import doesn't cause a circular reference

urlpatterns = [
    path('', views.product_list, name='product_list'),  # or any valid view
]
