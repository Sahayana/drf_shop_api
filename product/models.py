from django.db import models

# Create your models here.


class Category(models.Model):
    
    name        =   models.CharField(max_length= 50)


class Color(models.Model):

    name        =   models.CharField(max_length= 50)


class Featrue(models.Model):

    name        =   models.CharField(max_length= 500)


class Size(models.Model):

    name        =   models.CharField(max_length= 50)


class Image(models.Model):

    name        =   models.CharField(max_length= 500)


class Information(models.Model):

    origin      =   models.CharField(max_length= 50)
    composition =   models.CharField(max_length= 150, null= True, blank= True)
    fit         =   models.CharField(max_length= 150, null= True, blank= True)


class Detail(models.Model):

    name        =   models.CharField(max_length=100)
    feature     =   models.ForeignKey(Featrue, on_delete= models.SET_NULL, null= True)
    information =   models.ForeignKey(Information, on_delete= models.SET_NULL, null= True)
    is_main     =   models.BooleanField(default=False)


class Product(models.Model):

    detail      =   models.ForeignKey(Detail, on_delete= models.SET_NULL, null= True)
    price       =   models.DecimalField(max_digits= 10, decimal_places= 2)


class ProductColor(models.Model):

    product     =   models.ForeignKey(Product, on_delete= models.SET_NULL, null= True)
    color       =   models.ForeignKey(Product, on_delete= models.SET_NULL, null= True)
    image       =   models.OneToOneField(Image, on_delete= models.SET_NULL, null= True)
    

class ProductColorSize(models.Model):

    product_color   =   models.ForeignKey(ProductColor, on_delete= models.SET_NULL, null= True)
    size            =   models.ForeignKey(Size, on_delete= models.SET_NULL, null= True)
    amount          =   models.IntegerField()