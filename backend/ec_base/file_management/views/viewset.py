from django_filters.rest_framework.backends import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, ListModelMixin, UpdateModelMixin
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet

from ..filters.filemanagement import FileManagementListQueryFields
from ..models import FileManagement
from ..serializers.file_management import FileManagementCreateSlz, FileManagementListSlz, FileManagementRetrieveSlz, \
    FileManagementUpdateSlz
from ...auth.permissions.permission import IsApproved
from ...common.constant.view_action import BaseViewAction
from ...common.custom.exceptions import PermissionDenied
from ...common.serializer.custom_mixins import CustomDestroyMixin


class FileManagementViewSet(CreateModelMixin, RetrieveModelMixin, ListModelMixin, CustomDestroyMixin, UpdateModelMixin,
                            GenericViewSet):
    serializer_class = FileManagementCreateSlz
    parser_classes = (MultiPartParser, FormParser,)
    queryset = FileManagement.objects.all()
    permission_classes = (AllowAny,)
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    search_fields = FileManagementListQueryFields.SEARCH_FIELDS
    ordering_fields = FileManagementListQueryFields.ORDER_FIELDS
    ordering = FileManagementListQueryFields.ORDER_DEFAULT_FIELD
    filterset_fields = FileManagementListQueryFields.FILTERSET_FIELDS

    def get_serializer_class(self):
        slz_switcher = {
            BaseViewAction.CREATE: FileManagementCreateSlz,
            BaseViewAction.LIST: FileManagementListSlz,
            BaseViewAction.RETRIEVE: FileManagementRetrieveSlz,
            BaseViewAction.UPDATE: FileManagementUpdateSlz,
        }
        return slz_switcher.get(self.action, FileManagementListSlz)

    def get_permissions(self):
        perm_switcher = {
            BaseViewAction.LIST: (AllowAny,),
            BaseViewAction.RETRIEVE: (IsApproved,),
            BaseViewAction.CREATE: (IsApproved,),
            BaseViewAction.UPDATE: (IsApproved,),
            BaseViewAction.DESTROY: (IsApproved,),
        }
        self.permission_classes = perm_switcher.get(self.action)
        if self.permission_classes is None:
            raise PermissionDenied()

        return super().get_permissions()
