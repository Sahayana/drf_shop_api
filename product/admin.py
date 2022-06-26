from django.contrib import admin
from django.contrib.auth.models import Group
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
# Register your models here.


admin.site.unregister(Group)
admin.site.register(Category)
admin.site.register(Color)
admin.site.register(Feature)
admin.site.register(Size)
admin.site.register(Image)
admin.site.register(Information)
admin.site.register(Detail)
admin.site.register(Product)
admin.site.register(ProductColor)
admin.site.register(ProductColorSize)