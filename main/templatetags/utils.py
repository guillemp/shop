from django import template
from main import models

register = template.Library()

@register.simple_tag
def cart_count(request):
    return models.Cart.objects.all().count()

@register.assignment_tag
def cart_contains(request, product_id):
    return models.Cart.objects.filter(product_id=product_id).exists()

@register.simple_tag
def url_replace(request, field, value):
    dict_ = request.GET.copy()
    dict_[field] = value
    return dict_.urlencode()
