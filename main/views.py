from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from main import models
import random, string

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

def cart_remove(request):
    if request.POST:
        product_id = request.POST.get('product_id', 0)
        item = get_object_or_404(models.Cart, product_id=product_id).delete()
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


###############################################################################
# ADMIN VIEWS
###############################################################################


def order_id_generator(size=8, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))

def generate_code(request, responde=False):
    return HttpResponse(order_id_generator())



@login_required
def admin_view(request):
    return render(request, 'admin/index.html', {})


@login_required
def admin_products(request):
    products = models.Product.objects.all().order_by('-id')

    return render(request, 'admin/products.html', {
        "products": products
    })


@login_required
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

        messages.success(request, 'New product created.')
        return redirect('/admin/products/add/')

    return render(request, 'admin/products_add.html', {
        'code': order_id_generator()
    })

@login_required
def admin_products_edit(request, product_id):
    try:
        product = models.Product.objects.get(pk=product_id)
    except models.Product.DoesNotExist:
        raise Http404

    if request.POST:
        product.code = request.POST.get('code', '')
        product.description = request.POST.get('description', '')
        product.price = request.POST.get('price', 0)
        product.save()

        messages.success(request, 'Product saved.')
        return redirect('/admin/products/edit/{}'.format(product.id))

    return render(request, 'admin/products_edit.html', {
        "product": product
    })