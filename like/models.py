from django.db import models
from account.models import CustomUser

from product.models import ProductColor

# Create your models here.



class ProductLike(models.Model):

    user    = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductColor, on_delete=models.CASCADE)
    
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["user", "product"], name="unique_user_product"),
        ]