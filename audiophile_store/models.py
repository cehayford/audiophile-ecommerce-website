from django.db import models
from uuid import uuid4
import os

# Create your models here.
class Category(models.Model):
    type = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.type


class ProductImage(models.Model):
    mainimage = models.ImageField(upload_to='main/')
    firstimage = models.ImageField(upload_to='')
    secondimage = models.ImageField(upload_to='')
    thirdimage = models.ImageField(upload_to='')

    def __str__(self):
        return f'{self.mainimage}'
    
    def delete(self, *args, **kwargs):
        # Delete image files associated with image fields
        image_fields = [field for field in self._meta.fields if isinstance(field, models.ImageField)]
        for field in image_fields:
            file_path = getattr(self, field.name).path
            print(file_path)
            if os.path.exists(file_path):
                os.remove(file_path)
        super().delete(*args, **kwargs)


class Product(models.Model):
    Category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=9999.99)
    description = models.TextField(blank = True, default='product description...')
    features = models.TextField(blank =True, default='product features description...')
    Release_date = models.DateField(auto_now=True)
    image = models.ForeignKey(ProductImage, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'

    
class Cart(models.Model):
    cartid = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    date = models.DateField(auto_now_add=True)
    

class CartItem(models.Model):
    quantity = models.IntegerField(default=0)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='products')
    created = models.DateField(auto_now=True)
    modified = models.DateField(auto_now_add=True)
    shipping = models.BooleanField(default=False)



