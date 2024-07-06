from .serializers import *
from .models import Product, ProductImage
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_202_ACCEPTED, HTTP_400_BAD_REQUEST, HTTP_200_OK, HTTP_500_INTERNAL_SERVER_ERROR, HTTP_404_NOT_FOUND

# Create your views here.
class ProductDataView(APIView):
    def get(self, request):
        product = Product.objects.all()
        serializer = ProductDataSerializer(product, many=True)
        return Response(serializer.data)


# Product Image
class ProductImageView(APIView):
    def get(self, request):
        image = ProductImage.objects.all()
        serializer = ProductImageSerializer(image, many=True)
        return Response(serializer.data)


class CreateProductImageView(APIView):
    def get(self, request):
        # image = Product_images.objects.filter(id = pk).last()
        image = ProductImage.objects.filter().last()
        serializers = ProductImageSerializer(image)
        return Response(serializers.data)

    def post(self, request):
        try:
            serializer = ProductImageSerializer( data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status= HTTP_200_OK)
            return Response(serializer.errors)
        except Exception as e: return Response({'error': str(e)}, status= HTTP_500_INTERNAL_SERVER_ERROR)
        

class UpdateProductImageView(APIView):
    def put(self, request, pk):
        try:
            image = ProductImage.objects.get(id = pk)
            serializer = ProductImageSerializer(image, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=HTTP_202_ACCEPTED)
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
        except ProductImage.DoesNotExist as e:
            return Response({'error': str(e)}, status= HTTP_500_INTERNAL_SERVER_ERROR)

    def patch(self, request, pk):
        try:
            image = ProductImage.objects.get(id = pk)
            serializer = ProductImageSerializer(image, request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status= HTTP_202_ACCEPTED)
            return Response(serializer.errors, status= HTTP_400_BAD_REQUEST)
        except ProductImage.DoesNotExist as e:
            return Response({'error':str(e)}, status= HTTP_404_NOT_FOUND)


class DeleteProductImageView(APIView):
    def get(self, request, pk):
        try:
            image = ProductImage.objects.get(id = pk)
            serializer = ProductImageSerializer(image)
            return Response(serializer.data)
        except ProductImage.DoesNotExist:
            return Response({'error':'Product image(s) does not exist...'}, status= HTTP_404_NOT_FOUND)
    
    def delete(self, request, pk):
        try:
            image = ProductImage.objects.get(id = pk)
            if image:
                image.delete()
                return Response({'status':'the product image(s) were deleted...'}, status = HTTP_200_OK)
            return Response({'status':'the product images not found...'}, status= HTTP_404_NOT_FOUND)
        except ProductImage.DoesNotExist:
            return Response({'status':'the product images does not exist...'}, status= HTTP_404_NOT_FOUND)



#Product
class CreateProductView(APIView):
    def get(self, request):
        product = Product.objects.filter().last()
        serializers = ProductSerializer(product)
        return Response(serializers.data)

    def post(self, request):
        try:
            serializer = ProductSerializer( data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status= HTTP_200_OK)
            return Response(serializer.errors)
        except Exception as e: return Response({'error': str(e)}, status= HTTP_500_INTERNAL_SERVER_ERROR)
        

class UpdateProductView(APIView):
    def put(self, request, pk):
        try:
            product = Product.objects.get(id = pk)
            serializer = ProductSerializer(product, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=HTTP_202_ACCEPTED)
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
        except Product.DoesNotExist as e:
            return Response({'error': str(e)}, status= HTTP_500_INTERNAL_SERVER_ERROR)

    def patch(self, request, pk):
        try:
            product = Product.objects.get(id = pk)
            serializer = ProductSerializer(product, data = request.data, partial = True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status= HTTP_202_ACCEPTED)
            return Response(serializer.errors, status= HTTP_400_BAD_REQUEST)
        except Product.DoesNotExist as e:
            return Response({'error':str(e)}, status= HTTP_404_NOT_FOUND)


class DeleteProductView(APIView):
    def get(self, request, pk):
        try:
            product = Product.objects.get(id = pk)
            serializer = ProductSerializer(product)
            return Response(serializer.data)
        except Product.DoesNotExist:
            return Response({'error':'Product image(s) does not exist...'}, status= HTTP_404_NOT_FOUND)
    
    def delete(self, request, pk):
        try:
            image = Product.objects.filter(id = pk)
            if image:
                image.delete()
                return Response({'status':'the product image(s) were deleted...'}, status = HTTP_200_OK)
            return Response({'status':'the product images does not exist...'}, status= HTTP_404_NOT_FOUND)
        except Product.DoesNotExist:
            return Response({'status':'the product images does not exist...'}, status=HTTP_500_INTERNAL_SERVER_ERROR)


