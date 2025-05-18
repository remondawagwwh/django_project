from django.shortcuts import render, redirect, get_object_or_404
from .models import Category

def category_list(request):
    categories = Category.getall()
    return render(request, 'category/list.html', {'categories': categories})

def category_new(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        if name:
            Category.objects.create(name=name, description=description)
            return redirect('category_list')
    return render(request, 'category/new.html')

def category_update(request, id):
    category = get_object_or_404(Category, pk=id)
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        if name:
            category.name = name
            category.description = description
            category.save()
            return redirect('category_list')
    return render(request, 'category/update.html', {'category': category})

def category_delete(request, id):
    category = get_object_or_404(Category, pk=id)
    category.softdelete()
    return redirect('category_list')
