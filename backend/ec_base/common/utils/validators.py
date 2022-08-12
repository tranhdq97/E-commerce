from django.core.validators import BaseValidator
from django.utils.deconstruct import deconstructible

from ..constant import message


@deconstructible
class FileSizeValidator(BaseValidator):
    message = message.FILE_SIZE_EXCEED_LIMIT
    code = "invalid_file_size"

    def compare(self, a, b):
        return a > b * 1024 * 1024

    def clean(self, x):
        return x.size
