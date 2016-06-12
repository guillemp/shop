from django.conf.urls import include, url
from django.contrib import admin
from main import views

urlpatterns = [
    url(r'^$', views.index_view, name='index_view'),

    url(r'^cart/$', views.cart_view, name='cart_view'),
    url(r'^cart/add/$', views.cart_add, name='cart_add'),
    url(r'^cart/remove/$', views.cart_remove, name='cart_remove'),

    url(r'^checkout/$', views.checkout_view, name='checkout_view'),
    url(r'^admin/$', views.admin_view, name='admin_view'),
    url(r'^admin/products/$', views.admin_products, name='admin_products'),
    url(r'^admin/products/add/$', views.admin_products_add, name='admin_products_add'),
    url(r'^admin/products/edit/(?P<product_id>[0-9]+)/$', views.admin_products_edit, name='admin_products_edit'),
    url(r'^admin/products/generate_code/$', views.generate_code, name='generate_code'),

    url('^accounts/', include('django.contrib.auth.urls'))
]
