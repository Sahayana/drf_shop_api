from rest_framework import views, permissions, status
from rest_framework.response import Response
from account.serializer import CustomUserSerializer
# Create your views here.



class CustomUserView(views.APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        data = request.data
        serialzier = CustomUserSerializer(data=data)
        serialzier.is_valid(raise_exception=True)
        serialzier.save()
        return Response(serialzier.data, status=status.HTTP_201_CREATED)
        