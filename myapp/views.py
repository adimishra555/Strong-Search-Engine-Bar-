
from .models import Product
from .forms import ProductSearchForm, ProductForm
from django.shortcuts import render, redirect

from django.shortcuts import render
from django.http import JsonResponse
from .models import Product
from .forms import ProductSearchForm

def product_list(request):
    form = ProductSearchForm(request.GET)
    products = Product.objects.all()

    if form.is_valid():
        name = form.cleaned_data.get('name')
        price = form.cleaned_data.get('price')
        image = form.cleaned_data.get('image')
        created_at = form.cleaned_data.get('created_at')

        if name:
            products = products.filter(name__icontains=name)
        if price:
            products = products.filter(price=price)
        if image:
            products = products.filter(image=image)
        if created_at:
            products = products.filter(created_at=created_at)

        # if 'term' in request.GET:
        #     term = request.GET.get('term')
        # products = Product.objects.filter(name__icontains=term)
        # suggestions = list(products.values_list('name', flat=True))
        # return JsonResponse(suggestions, safe=False)

    return render(request, 'product_list.html', {'form': form, 'products': products})




def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})


