from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .apis import UserLoginApi, UserMeApi

urlpatterns = [
    path('login/', UserLoginApi.as_view(), name='login'),
    path('me/', UserMeApi.as_view(), name='me'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
]
