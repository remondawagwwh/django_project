from django.db import models
from category.models import Category
# Create your models here.
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    image = models.ImageField(upload_to='product/imgs', blank=True)  # لو مش بتتعامل مع رفع صور، استخدمي URL
    sku = models.CharField(max_length=50, unique=True)
    date_added = models.DateTimeField(auto_now_add=True)