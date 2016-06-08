from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from main import models

def index_view(request):
    products = models.Product.objects.all()
    u = request.user

    return render(request, 'index.html', {
        "products": products,
        'u': u,
    })

#
# Cart views
#
def cart_view(request):
    items = models.Cart.objects.all()

    return render(request, 'cart.html', {
        "items": items
    })

def cart_add(request):
    if request.POST:
        product_id = request.POST.get('product_id', 0)
        item = models.Cart.create_or_update(request, product_id)
        return HttpResponse("ok")

    return HttpResponse("error")


#
#
#
def checkout_view(request):
    products = models.Product.objects.all()

    return render(request, 'checkout.html', {
        "products": products
    })

#
# ADMIN VIEWS
#

def admin_view(request):
    return render(request, 'admin/index.html', {})

def admin_products(request):
    products = models.Product.objects.all()

    return render(request, 'admin/products.html', {
        "products": products
    })

def admin_products_add(request):
    if request.POST:
        code = request.POST.get('code', '')
        description = request.POST.get('description', '')
        price = request.POST.get('price', 0)

        product = models.Product()
        product.code = code
        product.description = description
        product.category_id = 1 # temp
        product.price = price
        product.save()

        return redirect('/admin/products/')

    return render(request, 'admin/products_add.html', {})

def admin_products_edit(request, product_id):
    return render(request, 'admin/products_edit.html', {
        "product": product_id
    })