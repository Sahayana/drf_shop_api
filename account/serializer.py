from attr import s
from rest_framework import serializers, status
from account.models import CustomUser
from account.services.customuser_service import create_single_user
from account.utils import email_validator, password_validator, phone_validator



class CustomUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CustomUser
        fields = ("id", "username", "password", "email", "fullname", "phone")
        extra_kwargs = {
            "password": {"write_only": True},
            "id": {"read_only": True}
        }


    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")
        phone = attrs.get("phone")

        if not email_validator(email=email):
            raise serializers.ValidationError(
                detail={"error": "올바른 이메일 주소를 입력하세요."}, 
                code=status.HTTP_400_BAD_REQUEST
                )
        elif not password_validator(password=password):
            raise serializers.ValidationError(
                detail={"error": "패스워드는 8자 이상, 특수문자 1개 이상 포함합니다."}, 
                code=status.HTTP_400_BAD_REQUEST
                )
        elif not phone_validator(phone=phone):
            raise serializers.ValidationError(
                detail={"error": "올바른 휴대전화번호를 입력하세요"}, 
                code=status.HTTP_400_BAD_REQUEST
            )
        
        return attrs
    
    
    def create(self, validated_data):
        valid_field = ["username", "password", "email", "fullname", "phone"]
        data = {key: value for key, value in validated_data.items() if key in valid_field}
        return create_single_user(**data)