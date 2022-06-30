from django.urls import path
from like.views import ProductLikeView

urlpatterns = [    
    path('likes', ProductLikeView.as_view()),     
]

