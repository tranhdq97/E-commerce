from rest_framework import serializers

from ec_base.common.constant import message
from ec_base.common.constant.db_fields import CommonFields, FileManagementFields
from ec_base.common.constant.master import MasterFileTypeID
from ec_base.common.utils.exceptions import APIErr
from ec_base.common.utils.serializer import ForeignKeyField
from ec_base.file_management.models import FileManagement
from ec_base.master.models import MasterFileType


class BaseFileManagementSlz(serializers.ModelSerializer):
    class Meta:
        model = FileManagement
        fields = (CommonFields.ID, FileManagementFields.FILE.value,)

    def validate(self, attrs):
        extension_switcher = {
            MasterFileTypeID.IMAGE: ("jpeg", "jpg", "gif", "svg", "png", "tiff", "tif"),
            MasterFileTypeID.DOCUMENT: ("pdf", "doc", "docx", "html", "htm", "xls", "xlsx", "txt"),
            MasterFileTypeID.VIDEO: ("mp4", "avi", "mov", "flv"),
            MasterFileTypeID.PRESENTATION: ("ppt", "pptx", "odp", "key"),
            MasterFileTypeID.AUDIO: ("m4a", "mp3", "wav"),
        }
        file = attrs.get(FileManagementFields.FILE).name
        file_ext = file.split('.')[-1]
        valid_extensions = extension_switcher.get(attrs.get(FileManagementFields.TYPE_ID))
        if valid_extensions and file_ext not in valid_extensions:
            raise APIErr(message.NOT_MATCHED_FILE_TYPE)

        return attrs


class FileManagementCreateSlz(BaseFileManagementSlz):
    type_id = ForeignKeyField(model=MasterFileType)

    class Meta:
        model = BaseFileManagementSlz.Meta.model
        fields = BaseFileManagementSlz.Meta.fields + (
            FileManagementFields.NAME, FileManagementFields.DESC, FileManagementFields.TYPE_ID,)


class FileManagementListSlz(BaseFileManagementSlz):
    type_id = ForeignKeyField(model=MasterFileType)

    class Meta:
        model = BaseFileManagementSlz.Meta.model
        fields = BaseFileManagementSlz.Meta.fields + (
            FileManagementFields.NAME, FileManagementFields.TYPE_ID,)


class FileManagementRetrieveSlz(BaseFileManagementSlz):
    type_id = ForeignKeyField(model=MasterFileType)

    class Meta:
        model = BaseFileManagementSlz.Meta.model
        fields = BaseFileManagementSlz.Meta.fields + \
                 (FileManagementFields.NAME, FileManagementFields.DESC, FileManagementFields.TYPE_ID,) + \
                 (CommonFields.CREATED_AT, CommonFields.UPDATED_AT,)


class FileManagementUpdateSlz(BaseFileManagementSlz):
    type_id = ForeignKeyField(model=MasterFileType, required=False)

    class Meta:
        model = BaseFileManagementSlz.Meta.model
        fields = BaseFileManagementSlz.Meta.fields + (
            FileManagementFields.NAME, FileManagementFields.DESC, FileManagementFields.TYPE_ID,)
        extra_kwargs = {FileManagementFields.FILE: {"required": False}}
