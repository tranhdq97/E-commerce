from django.db import models

from ...common.constant.app_label import ModelAppLabel
from ...common.constant.db_table import DBTable
from ...common.models.base import Creator, Editor, DateTimeModel
from ...common.utils.strings import get_file_field_directory
from ...common.utils.validators import FileSizeValidator
from ...master.models import MasterFileType


class FileManagement(Creator, Editor, DateTimeModel):
    UPLOAD_SIZE_LIMIT = 200  # 200MB

    name = models.CharField(max_length=256, null=True)
    desc = models.TextField(null=True)
    file = models.FileField(upload_to=get_file_field_directory, validators=[FileSizeValidator(UPLOAD_SIZE_LIMIT)])
    type = models.ForeignKey(MasterFileType, on_delete=models.RESTRICT, related_name=DBTable.FILE_MANAGEMENT)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = DBTable.FILE_MANAGEMENT
        app_label = ModelAppLabel.FILE_MANAGEMENT
