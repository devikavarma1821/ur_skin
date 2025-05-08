from django.contrib import admin
from .models import Product, CartItem, FavouriteItem

admin.site.register(Product)
admin.site.register(CartItem)
admin.site.register(FavouriteItem)

