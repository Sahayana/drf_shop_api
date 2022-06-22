from django.urls import path
from account.views import CustomUserView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [    
    path('accounts', CustomUserView.as_view()),
    path('accounts/token', TokenObtainPairView.as_view()),
    path('accounts/token/refresh', TokenRefreshView.as_view()), 
]

