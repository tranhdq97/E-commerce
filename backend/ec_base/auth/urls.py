from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from ec_base.auth.views.viewapi import change_password, get_me
from ec_base.auth.views.viewset import CustomTokenObtainPairView

urlpatterns = [
    path('token', CustomTokenObtainPairView.as_view(), name='token obtain pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token refresh'),
    path('get-me', get_me, name='get me'),
    path('change-password', change_password, name='change password'),
]
