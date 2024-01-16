from django.shortcuts import render,redirect
from store.models import product
from .models import Cart,Cartitem

# Create your views here.

def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart    


def add_cart(request, product_id):
    Product = product.objects.get(id=product_id) #get product
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request)) #get the cart using the cart id present in the session
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id = _cart_id(request)
        )
    cart.save()

    try:
        cart_item = Cartitem.objects.get(Product=Product, cart=cart)
        cart_item.quantity += 1      #cart_item.quantity = cart_item + 1
        cart_item.save()
    except cart_item.DoesNotExist:
        cart_item = Cartitem.objects.create(
            Product = Product,
            quantity = 1,
            cart = cart,
        )
        cart_item.save()
        
    return redirect('cart')    


def cart(request):
    return render(request, 'store/cart.html')