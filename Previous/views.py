from django.shortcuts import render, redirect, reverse, HttpResponseRedirect, get_object_or_404
from django.contrib import auth, messages
from .forms import SubscriptionForm, MakePaymentForm, OrderForm
from django.contrib.auth.decorators import login_required

from django.conf import settings
from django.utils import timezone
# import stripe

# stripe.api_key = settings.STRIPE_SECRET
#------------------------------------------------------------------------------- 

@login_required(login_url="/accounts/login")
def subscribe(request):
    subscription_form = SubscriptionForm()
    return render(request, 'subscription.html', {'subscription_form': subscription_form });
    
#------------------------------------------------------------------------------- 

# Need to add a single item (subscription) and make sure there is only one
# Needs to include the correct ID of the subscription

def add_to_cart(request):
    
    print('add_to_cart');
    
    sub_name = request.POST.get('name')
    print(sub_name)
    
    cart = request.session.get('cart', {})
    
    if len(cart) > 0:
        cart = {};
        
    cart[id] = cart.get(id, sub_name)
    
    print("here")
    print(sub_name)
    
    request.session['cart'] = cart    
    return redirect(subscribe)

#------------------------------------------------------------------------------- 

@login_required(login_url="/accounts/login")
def checkout(request):
    print('checkout')
    if request.method=="POST":
        print("if")
        # order_form = OrderForm(request.POST)
        # payment_form = MakePaymentForm(request.POST)
        
        # if order_form.is_valid() and payment_form.is_valid():
        #     order = order_form.save(commit=False)
        #     order.date = timezone.now()
        #     order.save()

            # cart = request.session.get('cart', {})
            # total = 0
            # for id, quantity in cart.items():
            #     subscription = get_object_or_404(Subscription, pk=id)
            #     total += quantity * product.price
            #     order_line_item = OrderLineItem(
            #         order = order,
            #         product = product,
            #         quantity = quantity
            #         )
            #     order_line_item.save()

            # try:
            #     customer = stripe.Charge.create(
            #         amount= int(total * 100),
            #         currency="EUR",
            #         description=request.user.email,
            #         card=payment_form.cleaned_data['stripe_id'],
            #     )
            # except stripe.error.CardError:
            #     messages.error(request, "Your card was declined!")

            # if customer.paid:
            #     messages.error(request, "You have successfully paid")
            #     request.session['cart'] = {}
            #     return redirect(reverse('all_products'))
            # else:
            #     messages.error(request, "Unable to take payment")
        # else:
            # print(subscription_form.errors)
            # messages.success(request, 'We were unable to take a payment with that card!', extra_tags='danger')
    else:
        print('else')
        # payment_form = MakePaymentForm()
        # order_form = OrderForm()

    # return render(request, 'subscription.html', {'subscription_form': subscription_form, 'order_form': order_form, 'payment_form': payment_form, 'publishable': settings.STRIPE_PUBLISHABLE })
    # return render(request, 'subscription.html', {'subscription_form': subscription_form })
    return redirect(subscribe)
    
#------------------------------------------------------------------------------- 