from django.contrib import admin 
from top_product.models import Products
# Register your models here.

class ProductsAdmin(admin.ModelAdmin):
    list_display=('id','name','image','user_rated','rating','price')

admin.site.register(Products,ProductsAdmin)
 

#Admin
#username=Admin
#password=admin@123