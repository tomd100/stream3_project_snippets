from django.shortcuts import render, redirect, reverse, HttpResponseRedirect, get_object_or_404
from django.contrib import auth, messages
from .forms import UserLoginForm, UserRegistrationForm, MakePaymentForm, OrderForm
from django.contrib.auth.decorators import login_required
from .models import Subscription

from django.conf import settings
from django.utils import timezone
import stripe

stripe.api_key = settings.STRIPE_SECRET

#-------------------------------------------------------------------------------

def home_page(request):
    return render(request, 'index.html')
    
#-------------------------------------------------------------------------------

def logout(request):
    auth.logout(request);                                                      
    messages.success(request, "You have successfully logged out")
    return redirect(home_page);
    
#-------------------------------------------------------------------------------

def login(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = auth.authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password'])
            if user is not None:
                auth.login(request, user);
                messages.success(request, "You have successfully logged in")                
                return redirect(profile)
            else:
                messages.success(request, "Your user name or password was not recognised ", extra_tags='danger') 
                # form.add_error(None, "Your user name or password was not recognised ")
    else:
        form = UserLoginForm();
    return render(request, "login.html", {'form': form})    
    
#-------------------------------------------------------------------------------    

def register(request):
    if request.method=="POST":
        form = UserRegistrationForm(request.POST);
        if form.is_valid():
            user = form.save();
            user = auth.authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'])
            if user is not None:
                auth.login(request, user);
                
                if request.GET and request.GET['next'] != "":
                    next = request.GET["next"];
                    return HttpResponseRedirect(next);
                else:
                    return redirect(login);
                
            return redirect(login)      
    else:
        form = UserRegistrationForm();

    return render(request, "register.html", {'form': form})
    
#-------------------------------------------------------------------------------


@login_required(login_url="/accounts/login")
def checkout(request):
    if request.method=="POST":
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
        payment_form = MakePaymentForm()
        order_form = OrderForm()

    return render(request, "checkout.html", {'order_form': order_form, 'payment_form': payment_form, 'publishable': settings.STRIPE_PUBLISHABLE })
    
#------------------------------------------------------------------------------- 

@login_required(login_url="/accounts/login")
def profile(request):
    return render(request, "profile.html");

#------------------------------------------------------------------------------- 