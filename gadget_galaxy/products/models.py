from django.db import models
from django.shortcuts import redirect
from category.models import Category

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    image = models.ImageField(upload_to='product/imgs', blank=True, null=True)
    sku = models.CharField(max_length=50, unique=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated= models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    @classmethod
    def getall(cls):
        return cls.objects.filter(status=True)

    @classmethod
    def get_by_id(cls, id):
        return cls.objects.get(pk=id)

    @classmethod
    def Add(cls, Pname, description, price, stock, Pimage, sku, catid):
        category_obj = Category.get_catagory_by_id(catid)
        Product.objects.create(
            category=category_obj,
            name=Pname,
            description=description,
            price=price,
            stock=stock,
            image=Pimage,
            sku=sku
        )

    @classmethod
    def harddel(cls, id):
        return cls.objects.filter(pk=id).delete()

    # @classmethod
    # def softdelete(cls, id):
    #     cls.objects.filter(pk=id).update(status=False)

    @staticmethod
    def go_to_Products_List():
        return redirect('product_list')

    def softdelete(self):
        self.status = False
        self.save()