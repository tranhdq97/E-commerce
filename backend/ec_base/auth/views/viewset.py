from rest_framework_simplejwt.views import TokenObtainPairView

from ec_base.auth.serializers.auth import CustomTokenObtainPairSerializer


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
