from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),  # قائمة المنتجات
    path('new/', views.product_new, name='product_new'),  # إضافة جديد
    path('update/<int:id>/', views.product_update, name='product_update'),  # تعديل
    path('delete/<int:id>/', views.product_delete, name='product_delete'),  # حذف (soft delete)
    path('details/<int:id>/', views.product_details, name='product_details'),  # تفاصيل المنتج
]
