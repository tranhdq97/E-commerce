from django.db import models

from backend.ec_base.common.models.base import DateTimeModel


class UserInfo(DateTimeModel):
    first_name = models.CharField(max_length=16)
    last_name = models.CharField(max_length=20)
