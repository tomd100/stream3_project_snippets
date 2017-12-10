from django.shortcuts import get_object_or_404
from .models import Subscription


def cart_contents(request):
    """
    Ensures that the cart contents are available when rendering every page. 
    """

    cart = request.session.get('cart', {})
    
    cart_items = []
    total = 0
    subscription_count = 0
    for id, quantity in cart.items():
        subscription = get_object_or_404(Subscription, pk=id)
        total += quantity * Subscription.price
        product_count += quantity
        cart_items.append({'id': id, 'quantity': quantity, 'subscription': subscription})

    return { 'cart_items': cart_items, 'total': total, 'subscription_count': subscription_count }