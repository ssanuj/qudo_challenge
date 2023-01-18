from django.contrib import admin
from .models import Product, Order  # import your models

# Register your models here.

admin.site.register(Product) # actual registration
admin.site.register(Order) # actual registration