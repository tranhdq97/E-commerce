from django.core.validators import BaseValidator
from django.utils.deconstruct import deconstructible

from ec_base.common.constant import message


@deconstructible
class FileSizeValidator(BaseValidator):
    message = message.FILE_SIZE_EXCEED_LIMIT
    code = "invalid_file_size"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.limit_value = self.limit_value * 1024

    def compare(self, a, b):
        return a > b

    def clean(self, x):
        return round(x.size / 1024)
