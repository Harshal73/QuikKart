from django.shortcuts import get_object_or_404, render
from .models import product
from category.models import category


def store(request, category_slug=None):
    categories = None
    products = None

    if category_slug != None:
        categories = get_object_or_404(category, slug=category_slug)
        products = product.objects.filter(category=categories, is_available=True)
        product_count = products.count()
    else:
        products = product.objects.all().filter(is_available=True)
        product_count = products.count()

    context = {
        'products':products,
        'product_count':product_count,
    }
    return render(request, 'store/store.html',context)
