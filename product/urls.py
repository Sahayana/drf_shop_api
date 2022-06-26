from django.urls import path
from product.views import (
    MainProductView,
    CategoryProductView,
    ProductDetailView
)

urlpatterns = [    
    path('products', MainProductView.as_view()),
    path('<str:category>', CategoryProductView.as_view()),
    path('products/<int:product_id>', ProductDetailView.as_view()), 
]

