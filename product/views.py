from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from product.serializer import ProductColorSerializer
from product.services.product_service import (
    get_main_products,
    get_category_products,
    get_single_product
)


# Create your views here.


class MainProductView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request, offset= 0, limit= 10):
        products = get_main_products(offset=offset, limit=limit)
        data = ProductColorSerializer(products, many=True).data
        return Response(data=data, status=status.HTTP_200_OK)


class CategoryProductView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, category, offset=0, limit=10):
        products = get_category_products(category=category, offset=offset, limit=limit)
        data = ProductColorSerializer(products, many=True).data
        return Response(data=data, status=status.HTTP_200_OK)


class ProductDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, product_id):
        product = get_single_product(product_id=product_id)
        data = ProductColorSerializer(product).data
        return Response(data=data, status=status.HTTP_200_OK)