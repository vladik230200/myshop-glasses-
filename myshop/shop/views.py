from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from basket.forms import BasketAddProductForm



def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    basket_product_form = BasketAddProductForm()
    if category_slug:
        language = request.LANGUAGE_CODE
        category = get_object_or_404(Category, translations__language_code=language, translations__slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'shop/product/list.html', {'category': category,
                                                      'categories': categories,
                                                      'products': products,
                                                      'basket_product_form': basket_product_form})


def product_detail(request, id, slug):
    language = request.LANGUAGE_CODE
    product = get_object_or_404(Product, id=id, translations__language_code=language, translations__slug=slug, available=True)
    basket_product_form = BasketAddProductForm()
    categories = Category.objects.all()
    return render(request, 'shop/product/detail.html', {'product': product,
                                                        'categories': categories,
                                                        'basket_product_form': basket_product_form})