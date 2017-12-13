from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import formset_factory, ModelChoiceField
from .models import Subscription, Order, OrderLineItem



#-------------------------------------------------------------------------------        

class SubscriptionChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return "%s -- €%s / %s" % (obj.description, obj.price, obj.type)
        # return "%s" % (obj.type)

class SubscriptionForm(forms.Form):
    select_sub = SubscriptionChoiceField(queryset=Subscription.objects.all(),
        widget = forms.Select(attrs = {'onchange' : "subText();"}))
    type = forms.CharField(required=True, max_length=20, initial='none')
    
#-------------------------------------------------------------------------------

class MakePaymentForm(forms.Form):

    MONTH_CHOICES = [(i, i,) for i in range(1, 13)]
    YEAR_CHOICES = [(i, i,) for i in range(2015, 2036)]

    credit_card_number = forms.CharField(label='Credit card number', required=False)
    cvv = forms.CharField(label='Security code (CVV)', required=False)
    expiry_month = forms.ChoiceField(label="Month", choices=MONTH_CHOICES, required=False)
    expiry_year = forms.ChoiceField(label="Year", choices=YEAR_CHOICES, required=False)
    stripe_id = forms.CharField(widget=forms.HiddenInput)
    
#-------------------------------------------------------------------------------

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('full_name', 'phone_number', 'country', 'postcode', 'town_or_city', 'street_address_1', 'street_address_2', 'county')

#-------------------------------------------------------------------------------        