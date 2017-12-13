from django.shortcuts import get_object_or_404
from .models import Subscription


def cart_contents(request):
    
    # del request.session['cart']
    # for key, value in request.session.items(): print('{} => {}'.format(key, value))
    
    sub_type = '';
    sub_desc = '';
    sub_price = 0;
    
    cart = request.session.get('cart', {})

    if cart:
        sub_type = cart['sub_type'];

        sub_obj = Subscription.objects.get(type = sub_type)
        sub_desc = sub_obj.description
        sub_price = sub_obj.price;
    
    return { 'sub_type': sub_type, 'sub_desc': sub_desc, 'sub_price': sub_price }