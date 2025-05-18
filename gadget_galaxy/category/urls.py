from django.urls import path
from . import views

urlpatterns = [
    path('', views.category_list, name='category_list'),
    path('new/', views.category_new, name='category_new'),
    path('update/<int:id>/', views.category_update, name='category_update'),
    path('delete/<int:id>/', views.category_delete, name='category_delete'),
]
