from rest_framework import serializers
from audiophile_store.models import Cart, CartItem
from decimal import Decimal

class CartSerializer(serializers.ModelSerializer):
    cartid = serializers.UUIDField(read_only=True)
    
    class Meta:
        model = Cart
        fields = ('cartid',)




class CartProductSerializer(serializers.ModelSerializer):
    totalprice = serializers.SerializerMethodField('get_total_price_with_vat',  read_only=True)

    class Meta:
        model = CartItem
        fields = '__all__'

    def get_total_amount(self, obj):
        # calculate the total cost of the items in the cart
        # return sum(item.product.price * item.quantity  for item in CartItem.objects.filter(cart = obj.cart))
        return sum(item.product.price * item.quantity  for item in obj.cart.products.all())
    

    def get_vat_on_total_price(self, obj):
        # calculate VAT on the total cost of the items in the cart plus additional charges
        # additional_price = sum(50 * item.quantity  for item in CartItem.objects.filter(cart = obj.cart))
        VAT = self.get_total_amount(obj) * Decimal(0.20)
        return VAT
    

    def get_total_price_with_vat(self, obj) -> str:
        # calculate VAT plus total cost of the items in the cart
        cost = self.get_vat_on_total_price(obj) + self.get_total_amount(obj) 
        if obj.shipping:
            ad_cost=cost + 50
        else:
            ad_cost=cost
        return round(ad_cost, 2)
