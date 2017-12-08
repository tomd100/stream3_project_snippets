from django.shortcuts import render, redirect, reverse, HttpResponseRedirect, get_object_or_404
from django.contrib import auth, messages
from .forms import SubscriptionForm,MakePaymentForm, OrderForm
from django.contrib.auth.decorators import login_required
# from .models import Subscription

from django.conf import settings
from django.utils import timezone
import stripe

stripe.api_key = settings.STRIPE_SECRET
#------------------------------------------------------------------------------- 

@login_required(login_url="/accounts/login")
def checkout(request):
    if request.method=="POST":
        subscription_form = SubscriptionForm(request.Post)
        order_form = OrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)
        
        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.save()

            cart = request.session.get('cart', {})
            total = 0
            # for id, quantity in cart.items():
            #     subscription = get_object_or_404(Subscription, pk=id)
            #     total += quantity * product.price
            #     order_line_item = OrderLineItem(
            #         order = order,
            #         product = product,
            #         quantity = quantity
            #         )
            #     order_line_item.save()

            try:
                customer = stripe.Charge.create(
                    amount= int(total * 100),
                    currency="EUR",
                    description=request.user.email,
                    card=payment_form.cleaned_data['stripe_id'],
                )
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")

            if customer.paid:
                messages.error(request, "You have successfully paid")
                request.session['cart'] = {}
                return redirect(reverse('all_products'))
            else:
                messages.error(request, "Unable to take payment")
        else:
            print(payment_form.errors)
            messages.error(request, "We were unable to take a payment with that card!")
    else:
        subscription_form = SubscriptionForm()
        payment_form = MakePaymentForm()
        order_form = OrderForm()

    return render(request, 'subscription.html', {'subscription_form': subscription_form, 'order_form': order_form, 'payment_form': payment_form, 'publishable': settings.STRIPE_PUBLISHABLE })
    
#------------------------------------------------------------------------------- 



# Capture selection when in view
# <form action="PageObjects" method="post">
#   <select >
#     <option selected="selected" disabled>Objects on page:</option>
#     <option value="10">10</option>
#     <option value="20">20</option>
#     <option value="30">30</option>
#     <option value="40">40</option>
#     <option value="50">50</option>
#   </select>
#   <input type="submit" value="Select">
# </form>

# def page_objects(request):
#   if request.method == 'POST':
#     form = YourForm(request.POST)

#     if form.is_valid():
#       answer = form.cleaned_data['value']