from django.contrib.auth.backends import BaseBackend

from ec_base.common.constant import message
from ec_base.common.constant.auth import UserEnum, get_user_model_by_provider
from ec_base.common.utils.exceptions import APIErr


class ModelBackend(BaseBackend):
    def authenticate(self, request, **kwargs):
        if request is None:
            return

        provider = request.data.get(UserEnum.PROVIDER)
        user_model = get_user_model_by_provider(provider=provider)
        username = kwargs.get(user_model.USERNAME_FIELD)
        password = kwargs.get('password')
        if not username or not password:
            return

        try:
            user = user_model._default_manager.get_by_natural_key(username)
        except user_model.DoesNotExist:
            raise APIErr(message.EMAIL_OR_PASSWORD_IS_INCORRECT)
        else:
            return self.validate_user(user, password)

    def validate_user(self, user, password):
        if not user.check_password(password):
            raise APIErr(message.EMAIL_OR_PASSWORD_IS_INCORRECT)

        # TODO: Check verifying status of email
        return user
