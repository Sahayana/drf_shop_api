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


class Featrue(models.Model):

    feature        =   models.CharField(max_length= 500)

    def __str__(self) -> str:
        return self.name


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


class Detail(models.Model):

    name        =   models.CharField(max_length=100)
    feature     =   models.ForeignKey(Featrue, on_delete= models.SET_NULL, null= True)
    information =   models.ForeignKey(Information, on_delete= models.SET_NULL, null= True)
    is_main     =   models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name


class Product(models.Model):

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
    

class ProductColorSize(models.Model):

    product_color   =   models.ForeignKey(ProductColor, on_delete= models.SET_NULL, null= True)
    size            =   models.ForeignKey(Size, on_delete= models.SET_NULL, null= True)
    quantity        =   models.IntegerField()