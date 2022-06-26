from product.models import ProductColor



def get_single_product(product_id: int):
    return (
        ProductColor.objects.select_related(
            "product",
            "product__category",
            "product__detail",
            "product__detail__feature",
            "product__detail__information",
            "color",
            "image"
        ).filter(id= product_id).prefetch_related("size").get()       
        )


def get_main_products(offset: int, limit: int):
    return (
        ProductColor.objects.select_related(
            "product",
            "product__category",
            "product__detail",
            "product__detail__feature",
            "product__detail__information",
            "color",
            "image"
        ).filter(product__detail__is_main= True).prefetch_related("size").all()
        [offset: offset + limit]        
    )


def get_category_products(category: str, offset: int, limit: int):
    return (
        ProductColor.objects.select_related(
            "product",
            "product__category",
            "product__detail",
            "product__detail__feature",
            "product__detail__information",
            "color",
            "image"
        ).filter(product__category__name__in= [category]).prefetch_related("size").all()
        [offset: offset + limit]
    )