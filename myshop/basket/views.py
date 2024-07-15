from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Product
from .basket import Basket
from .forms import BasketAddProductForm
from coupons.forms import CouponApplyForm


@require_POST
def basket_add(request, product_id):
    basket = Basket(request)
    product = get_object_or_404(Product, id=product_id)
    form = BasketAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        basket.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    else: print("not")
    return redirect('basket:basket_detail')


def basket_remove(request, product_id):
    print(request)
    basket = Basket(request)
    product = get_object_or_404(Product, id=product_id)
    basket.remove(product)
    return redirect('basket:basket_detail')


def basket_detail(request):
    basket = Basket(request)
    for item in basket:
        item['update_quantity_form'] = BasketAddProductForm(
                            initial={'quantity': item['quantity'],
                            'update': True})
    coupon_apply_form = CouponApplyForm()
    return render(request,
                  'basket/detail.html',
                  {'basket': basket,
                   'coupon_apply_form': coupon_apply_form})


def basket_clear(request):
    basket = Basket(request)
    basket.clear()
    return redirect('basket:basket_detail')