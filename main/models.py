from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.http import Http404


class Category(models.Model):
    name = models.CharField(max_length=64)

class Product(models.Model):
    code = models.CharField(max_length=32)
    description = models.CharField(max_length=128)
    category = models.ForeignKey(Category)
    status = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    ean = models.CharField(max_length=32)
    stock = models.IntegerField(default=0)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(null=True, blank=True)

class Customer(models.Model):
    telephone = models.CharField(max_length=32)
    ip = models.CharField(max_length=32)

class Country(models.Model):
    name = models.CharField(max_length=128)
    iso_code_2 = models.CharField(max_length=2)
    iso_code_3 = models.CharField(max_length=3)

class Region(models.Model):
    name = models.CharField(max_length=128)
    country = models.ForeignKey(Country)

class Address(models.Model):
    customer = models.ForeignKey(Customer)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    company = models.CharField(max_length=64, null=True, blank=True)
    phone = models.CharField(max_length=32, null=True, blank=True)
    address_1 = models.CharField(max_length=128)
    address_2 = models.CharField(max_length=128, null=True, blank=True)
    city = models.CharField(max_length=128)
    zipcode = models.CharField(max_length=16)
    country = models.ForeignKey(Country)
    region = models.ForeignKey(Region)

class Cart(models.Model):
    customer = models.ForeignKey(Customer, null=True, blank=True)
    session = models.CharField(max_length=64)
    product = models.ForeignKey(Product)
    quantity = models.IntegerField(default=0)
    created = models.DateTimeField(default=timezone.now)

    '''
    def get_total(self):
        total = 0
        cart_items = self.get_cart_items()
        for item in cart_items:
            total += (item.quantity * item.price)
        self.total = total
    '''

    @classmethod
    def create_or_update(cls, request, product_id):
        try:
            product = Product.objects.get(pk=product_id)
        except Product.DoesNotExist:
            raise Http404

        session = request.session
        session.save()

        item, created = Cart.objects.get_or_create(
            product=product,
            session=session.session_key
        )

        if created:
            item.quantity = 1
            item.save()
        elif not created:
            item.quantity += 1
            item.save()

        return item

class Order(models.Model):
    code = models.CharField(max_length=32)
    customer = models.ForeignKey(Customer)
    status = models.IntegerField(default=0)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(null=True, blank=True)

class OrderItem(models.Model):
    order = models.ForeignKey(Order)
    product = models.ForeignKey(Product)
    quantity = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    total = models.DecimalField(max_digits=8, decimal_places=2)

class OrderHistory(models.Model):
    order = models.ForeignKey(Order)
    status = models.IntegerField(default=0)
    created = models.DateTimeField(default=timezone.now)
