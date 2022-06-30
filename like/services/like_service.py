

from like.models import ProductLike


def product_like(user_id: int, product_id: int):
    return ProductLike.objects.create(user_id=user_id, product_id=product_id)


def product_unlike(user_id: int, product_id: int):
    ProductLike.objects.filter(user_id=user_id, product_id=product_id).delete()
