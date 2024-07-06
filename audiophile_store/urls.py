from django.urls import path, include
from .views import *

urlpatterns = [
    path('product', ProductDataView.as_view(), name='Product'),
    # product images
    path('product/image', ProductImageView.as_view(), name='Product'),
    path('product/create/image', CreateProductImageView.as_view(), name='create_product_image'),
    path('product/image/<str:pk>/update', UpdateProductImageView.as_view(), name='update_product_image'),
    path('product/image/<str:pk>/remove', DeleteProductImageView.as_view(), name='delete_product_image'),
    # products
    
    path('product/create', CreateProductView.as_view(), name='add_product'),
    path('product/<str:pk>/update', UpdateProductView.as_view(), name='update_product'),
    path('product/<str:pk>/remove', DeleteProductView.as_view(), name='remove_product'),

    path('cart/', include('cart.urls')),
]
