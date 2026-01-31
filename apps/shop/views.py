from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from apps.shop.models import Product


def index(request):
    return HttpResponse("Hello World. You're at the polls index.")


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'shop/details.html', {"product": product})


def user_detail(request, user_id):
    response = "You're looking at user %s."
    return HttpResponse(response % user_id)


# def home(request):
#     products = Product.objects.all()
#     template = loader.get_template("shop/home.html")
#     context = {"products_list": products}
#     return HttpResponse(template.render(context, request))


def home(request):
    products = Product.objects.all()[:20]
    context = {'products_list': products}
    return render(request, "shop/home.html", context)
