from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions

from like.serializer import ProductLikeSerializer
from like.services.like_service import product_unlike


# Create your views here.


class ProductLikeView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        data = {
            "product": request.data.get("product_id")
        }
        context = {
            "request": request
        }
        serializer = ProductLikeSerializer(data=data, context=context)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def delete(self, request):
        request_schema = {
            "user_id": request.user.id,
            "product_id": request.data.get("product_id")
        }
        product_unlike(**request_schema)
        return Response({"detail": "SUCCESS"}, status=status.HTTP_200_OK)

