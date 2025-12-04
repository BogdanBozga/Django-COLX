from django.http import HttpResponse
from django.shortcuts import render

from shop.models import Product

def index(request):
    return HttpResponse("Hello World. You're at the polls index.")

def product_detail(request, product_id):
    response = "You're looking at product %s."
    return HttpResponse(response % product_id)

def user_detail(request, user_id):
    response = "You're looking at user %s."
    return HttpResponse(response % user_id)

def home(request):
    products = Product.objects.all()
    return HttpResponse(products)
