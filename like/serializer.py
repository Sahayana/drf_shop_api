from rest_framework import serializers
from account.serializer import CustomUserSerializer
from like.models import ProductLike
from like.services.like_service import product_like
from product.serializer import ProductColorSerializer




class ProductLikeSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True)
    
    class Meta:
        model = ProductLike
        fields = ["user", "product"]
    

    def to_representation(self, instance):
        res = super().to_representation(instance=instance)
        res["product"] = ProductColorSerializer(instance.product).data
        return res
    

    def create(self, validated_data):
        data = {
            "user_id": self.context["request"].user.id,
            "product_id": validated_data["product"].id
        }
        return product_like(**data)


