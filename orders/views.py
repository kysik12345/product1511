import json
import uuid
from itertools import product

from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404, redirect, reverse
from django.http import JsonResponse

from orders.models import Order, OrderItem

from cart.views import Cart
from app.models import Product


@csrf_exempt
def new_order(request):
    data = json.loads(request.body)
    name = data.get('name')
    last_name = data.get('lastName')
    email = data.get('email')
    phone = data.get('phone')
    delivery = data.get('delivery')
    payment = data.get('payment')

    cart = Cart(request)
    order = Order.objects.create(name=name,
                         last_name=last_name,
                         email=email,
                         phone=phone,
                         delivery=delivery,
                         payment=payment,
                         number=uuid.uuid4(),
                        )
    for item in cart:
        OrderItem.objects.create(order=order, product=item['product'], quantity=item['quantity'])

    # orders = OrderItem.objects.filter(order=order)
    # cart_order = cart.copy()
    cart.clear()

    url = reverse("main")
    json_response = {"status": "ok", "url": url}
    return JsonResponse(json_response)

    
