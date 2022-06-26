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
        model  = Category
        fields = ["name"]


class ColorSerializer(serializers.ModelSerializer):

    class Meta:
        model  = Color
        fields = ["name"]


class FeatrueSerializer(serializers.ModelSerializer):

    class Meta:
        model  = Feature
        fields = ["feature"]


class SizeSerializer(serializers.ModelSerializer):

    class Meta:
        model  = Size
        fields = ["name"]


class ImageSerialzier(serializers.ModelSerializer):

    class Meta:
        model  = Image
        fields = ["image"]
        

class InformationSerializer(serializers.ModelSerializer):

    class Meta:
        model   = Information
        exclude = ["id"]


class DetailSerializer(serializers.ModelSerializer):

    feature     = serializers.StringRelatedField(read_only= True)
    information = InformationSerializer(read_only= True)

    class Meta:
        model   = Detail
        exclude = ["id"]


class ProductSerializer(serializers.ModelSerializer):

    category    = serializers.StringRelatedField(read_only= True)
    detail      = DetailSerializer(read_only= True)
    color_list  = serializers.SerializerMethodField(read_only= True)

    class Meta:
        model   = Product
        exclude = ["id", "color"]
    
    def get_color_list(self, obj):
        return [color.name for color in obj.color.all()]



class ProductColorSerializer(serializers.ModelSerializer):

    product = ProductSerializer(read_only= True)
    color   = serializers.StringRelatedField(read_only= True)
    image   = serializers.StringRelatedField(read_only= True)    
    size    = serializers.SerializerMethodField(read_only= True)

    class Meta:
        model = ProductColor
        fields = "__all__"        

    def get_size(self, obj):
        return [size.name for size in obj.size.all()]
    


class ProductColorSizeSerializer(serializers.ModelSerializer):

    product_color = ProductColorSerializer(read_only= True)
    size          = SizeSerializer(read_only= True)

    class Meta:
        model = ProductColorSize
        fields = "__all__"