from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, 'You basket is empty!')
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51Kj94NCeIcEdB7DZ1twnEEMo7Dj3R6ww99f7BqaSo87moomnPej3J40EL866gCjrHmyJk5jzv6PGDmpIjj5l7dMt00GpCDEG2N',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)