from ec_base.common.constant.db_fields import CommonFields, FileManagementFields


class FileManagementListQueryFields:
    SEARCH_FIELDS = (
        FileManagementFields.NAME,
        FileManagementFields.FILE,
    )
    ORDER_FIELDS = (
        CommonFields.ID,
        FileManagementFields.NAME,
        FileManagementFields.FILE,
        FileManagementFields.TYPE_ID,
    )
    ORDER_DEFAULT_FIELD = f"-{CommonFields.CREATED_AT}"
    FILTERSET_FIELDS = (FileManagementFields.TYPE_ID,)
