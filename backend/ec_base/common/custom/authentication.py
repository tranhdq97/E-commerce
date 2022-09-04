from drf_spectacular.contrib.rest_framework_simplejwt import SimpleJWTScheme
from rest_framework_simplejwt.authentication import JWTAuthentication

from ec_base.common.constant.auth import UserEnum, get_user_model_by_provider


class CustomJWTAuthentication(JWTAuthentication):
    def get_user(self, validated_token):
        provider = validated_token.get(UserEnum.PROVIDER)
        self.user_model = get_user_model_by_provider(provider=provider)
        user = super().get_user(validated_token)
        setattr(user, UserEnum.PROVIDER, provider)
        return user


class SimpleJWTTokenUserScheme(SimpleJWTScheme):
    target_class = CustomJWTAuthentication
