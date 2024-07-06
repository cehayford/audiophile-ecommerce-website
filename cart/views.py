from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CartSerializer, CartProductSerializer 
from audiophile_store.models import Cart, CartItem
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND, HTTP_500_INTERNAL_SERVER_ERROR


# Create your views here.
class CartView(APIView):
    def get(self, request):
        cart = Cart.objects.all()
        serializer = CartSerializer(cart, many=True)
        return Response(serializer.data)


class CreateCartView(APIView):
    def post(self, request):
        try:
            serializer = CartSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status = HTTP_200_OK)
        except Exception as e: 
            return Response({'error': str(e)}, status= HTTP_500_INTERNAL_SERVER_ERROR)


class DeleteCartView(APIView):
    def delete(self, request, cartID):
        try:
            cart = Cart.objects.get(cartid=cartID)
            if cart:
                cart.delete()
                return Response({'success': 'Cart have been deleted...'}, status= HTTP_200_OK)
            return Response({'error': 'Cart Id not found...'}, status = HTTP_404_NOT_FOUND)
        except Cart.DoesNotExist:
            return Response({'status':'Cart container was not created...'}, status= HTTP_404_NOT_FOUND)
        except Exception as e: 
            return Response({'status': str(e)}, status= HTTP_500_INTERNAL_SERVER_ERROR)


class CartProductView(APIView):
    def get(self, request):
        cartitem = CartItem.objects.all()
        serializer = CartProductSerializer(cartitem, many=True)
        return Response(serializer.data)


class CreateCartProductView(APIView):
    def get(self, request, pk):
        cartitem = CartItem.objects.filter(cart_id = pk)
        serializer = CartProductSerializer(cartitem, many = True)
        return Response(serializer.data)
    
    def post(self, request, pk):
        # try:
            serializer = CartProductSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status = HTTP_200_OK)
            return Response(serializer.errors)
        # except Exception as e:
        #     return Response({'status': str(e)}, status = HTTP_500_INTERNAL_SERVER_ERROR)


class UpdateCartProductView(APIView):
    def put(self,request, pk, cartid):
        try:
            cart = CartItem.objects.get(cart_id = cartid, id = pk)
            serializer = CartProductSerializer(cart, data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status= HTTP_200_OK)
            return Response(serializer.errors, status= HTTP_404_NOT_FOUND)
        except CartItem.DoesNotExist:
            return Response({'status': 'Cart item not found...'}, status= HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'status': str(e)}, status = HTTP_500_INTERNAL_SERVER_ERROR)

    def patch(self,request, pk, cartid):
        try:
            cart = CartItem.objects.get(cart_id=cartid,  id=pk)
            serializer = CartProductSerializer(cart, data = request.data, partial = True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status= HTTP_200_OK)
            return Response(serializer.errors, status= HTTP_404_NOT_FOUND)
        except CartItem.DoesNotExist:
            return Response({'status': 'Cart item not found...'}, status= HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'status': str(e)}, status = HTTP_500_INTERNAL_SERVER_ERROR)


class DeleteCartProductView(APIView):
    def delete(self, request, pk, cartid):
        try:
            cartitem = CartItem.objects.get(cart_id = cartid, id = pk)
            if cartitem:
                cartitem.delete()
                return Response({'success': 'Product have been deleted from the cart successfully...'},     status= HTTP_200_OK)
            return Response({'error': 'Product was not added to the cart...'}, status = HTTP_404_NOT_FOUND)
        except CartItem.DoesNotExist:
            return Response({'status':'Product do not exist in the cart...'}, status= HTTP_404_NOT_FOUND)
        except Exception as e: 
            return Response({'status': str(e)}, status= HTTP_500_INTERNAL_SERVER_ERROR)


