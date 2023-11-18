from django.contrib import admin

from products.models import Product

# this will make sure Product module appears in admin panel http://localhost:8000/admin/products/product/
admin.site.register(Product)
