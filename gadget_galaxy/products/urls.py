from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('new/', views.product_new, name='product_new'),
    path('update/<int:id>/', views.product_update, name='product_update'),
    path('delete/<int:id>/', views.product_delete, name='product_delete'),
    path('details/<int:id>/', views.product_details, name='product_details'),
]
