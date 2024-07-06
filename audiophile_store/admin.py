from django.contrib import admin
from .models import *

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("type", "slug",)

class ProductImageAdmin(admin.ModelAdmin):
    list_display = ("mainimage", "firstimage", "secondimage", "thirdimage",)

class ProductAdmin(admin.ModelAdmin):
    list_display = ("Category", "slug", "name", "price", "Release_date", "image",)

admin.site.register(Category, CategoryAdmin)
admin.site.register(ProductImage, ProductImageAdmin)
admin.site.register(Product, ProductAdmin)