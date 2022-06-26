from rest_framework import serializers
from product.models import (
    Category,
    Color,
    Feature,
    Size,
    Image,
    Information,
    Detail,
    Product,
    ProductColor,
    ProductColorSize
)



class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        models = Category
        fields = ["name"]


class ColorSerializer(serializers.ModelSerializer):

    class Meta:
        models = Color
        fields = ["name"]


class FeatrueSerializer(serializers.ModelSerializer):

    class Meta:
        models = Feature
        fields = ["feature"]


class SizeSerializer(serializers.ModelSerializer):

    class Meta:
        models = Size
        fields = ["name"]


class ImageSerialzier(serializers.ModelSerializer):

    class Meta:
        models = Image
        fields = ["image"]
        

class InformationSerializer(serializers.ModelSerializer):

    class Meta:
        models = Information
        fields = "__all__"


class DetailSerializer(serializers.ModelSerializer):

    feature     = FeatrueSerializer(read_only= True)
    information = InformationSerializer(read_only= True)

    class Meta:
        models = Detail
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):

    detail  = DetailSerializer(read_only= True)
    color   = ColorSerializer(many= True, read_only= True)

    class Meta:
        models = Product
        fields = "__all__"


class ProductColorSerializer(serializers.ModelSerializer):

    product = ProductSerializer(read_only= True)
    color   = ColorSerializer(read_only= True)
    image   = serializers.StringRelatedField(read_only= True)
    size    = SizeSerializer(many= True, read_only= True)

    class Meta:
        models = ProductColor
        fields = "__all__"


class ProductColorSizeSerializer(serializers.ModelSerializer):

    product_color = ProductColorSerializer(read_only= True)
    size          = SizeSerializer(read_only= True)

    class Meta:
        models = ProductColorSize
        fields = "__all__"