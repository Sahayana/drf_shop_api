from unicodedata import category
from django.db import models

# Create your models here.


class Category(models.Model):
    
    name        =   models.CharField(max_length= 50)

    def __str__(self) -> str:
        return self.name


class Color(models.Model):

    name        =   models.CharField(max_length= 50)

    def __str__(self) -> str:
        return self.name


class Feature(models.Model):

    feature        =   models.CharField(max_length= 500)

    def __str__(self) -> str:
        return self.feature


class Size(models.Model):

    name        =   models.CharField(max_length= 50)

    def __str__(self) -> str:
        return self.name


class Image(models.Model):

    image        =   models.CharField(max_length= 500)

    def __str__(self) -> str:
        return self.image


class Information(models.Model):

    origin      =   models.CharField(max_length= 50)
    composition =   models.CharField(max_length= 150, null= True, blank= True)
    fit         =   models.CharField(max_length= 150, null= True, blank= True)

    def __str__(self) -> str:
        return self.composition


class Detail(models.Model):

    name        =   models.CharField(max_length=100)
    feature     =   models.ForeignKey(Feature, on_delete= models.SET_NULL, null= True)
    information =   models.ForeignKey(Information, on_delete= models.SET_NULL, null= True)
    is_main     =   models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name


class Product(models.Model):

    category    =   models.ForeignKey(Category, on_delete= models.SET_NULL, null= True)
    detail      =   models.ForeignKey(Detail, on_delete= models.SET_NULL, null= True)
    price       =   models.DecimalField(max_digits= 10, decimal_places= 2)
    color       =   models.ManyToManyField(Color, through= "ProductColor")

    def __str__(self) -> str:
        return self.detail.name


class ProductColor(models.Model):
    
    product     =   models.ForeignKey(Product, on_delete= models.SET_NULL, null= True)
    color       =   models.ForeignKey(Color, on_delete= models.SET_NULL, null= True)
    image       =   models.OneToOneField(Image, on_delete= models.SET_NULL, null= True)
    size        =   models.ManyToManyField(Size, through= "ProductColorSize")
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["product", "color"], name="unique_product_color"),
        ]

    def __str__(self) -> str:
        return f"{self.product.detail.name}/ Color: {self.color.name}"


class ProductColorSize(models.Model):

    product_color   =   models.ForeignKey(ProductColor, on_delete= models.SET_NULL, null= True)
    size            =   models.ForeignKey(Size, on_delete= models.SET_NULL, null= True)
    quantity        =   models.IntegerField()


    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["product_color", "size"], name="unique_product_color_size"),
        ]

    
    def __str__(self) -> str:
        return f"{self.product_color.product.detail.name}/ Color: {self.product_color.color.name}/ Size: {self.size.name}"