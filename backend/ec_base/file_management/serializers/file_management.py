from rest_framework import serializers

from ec_base.common.constant.db_fields import CommonFields, FileManagementFields
from ec_base.file_management.models import FileManagement


class FileManagementPthSlz(serializers.ModelSerializer):
    class Meta:
        model = FileManagement
        fields = (CommonFields.ID, FileManagementFields.FILE,)
