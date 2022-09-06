from django.db import models

from ec_base.common.constant.app_label import ModelAppLabel
from ec_base.common.constant.db_table import DBTable
from ec_base.common.models.base import DateTimeModel
from ec_base.common.utils.strings import get_file_field_directory
from ec_base.common.utils.validators import FileSizeValidator
from ec_base.master.models import MasterFileType


class FileManagement(DateTimeModel):
    UPLOAD_SIZE_LIMIT = 200  # 200MB

    name = models.CharField(max_length=256, null=True)
    desc = models.TextField(null=True)
    file = models.FileField(upload_to=get_file_field_directory, validators=[FileSizeValidator(UPLOAD_SIZE_LIMIT)])
    type = models.ForeignKey(MasterFileType, on_delete=models.RESTRICT, related_name=DBTable.FILE_MANAGEMENT)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = DBTable.FILE_MANAGEMENT
        app_label = ModelAppLabel.FILE_MANAGEMENT
