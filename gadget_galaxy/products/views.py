from django.shortcuts import render, redirect, get_object_or_404
from category.models import Category
from .models import Product

def product_list(request):
    products = Product.getall()
    return render(request, 'products/list.html', {'products': products})

def product_new(request):
    catagories = Category.objects.all()
    if request.method == 'POST':
        Pname = request.POST.get('Pname')
        description = request.POST.get('description')
        price = request.POST.get('price')
        stock = request.POST.get('stock')
        Pimage = request.FILES.get('Pimage')
        sku = request.POST.get('sku')
        bcat = request.POST.get('bcat')

        catagoryobj = Category.objects.get(pk=bcat)

        Product.objects.create(
            category=catagoryobj,
            name=Pname,
            description=description,
            price=price,
            stock=stock,
            image=Pimage,
            sku=sku,
        )
        return redirect('product_list')

    return render(request, 'products/new.html', {'catagories': catagories})

def product_update(request, id):
    product = get_object_or_404(Product, pk=id)
    catagories = Category.objects.all()
    if request.method == 'POST':
        product.name = request.POST.get('Pname')
        product.description = request.POST.get('description')
        product.price = request.POST.get('price')
        product.stock = request.POST.get('stock')
        sku = request.POST.get('sku')
        product.sku = sku
        bcat = request.POST.get('bcat')
        product.category = Category.objects.get(pk=bcat)

        if 'Pimage' in request.FILES:
            product.image = request.FILES['Pimage']

        product.save()
        return redirect('product_list')

    return render(request, 'products/update.html', {'product': product, 'catagories': catagories})

def product_delete(request, id):
    product = get_object_or_404(Product, pk=id)
    if request.method == 'POST':  # Always use POST for destructive actions
        product.softdelete()
        return redirect('product_list')
    return render(request, 'products/list.html', {'product': product})

def product_details(request, id):
    product = get_object_or_404(Product, pk=id)
    return render(request, 'products/details.html', {'product': product})
