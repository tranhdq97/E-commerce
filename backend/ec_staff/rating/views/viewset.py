from django_filters.rest_framework.backends import DjangoFilterBackend
from rest_framework import mixins
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet

from ec_base.auth.permissions.permission import IsManager, IsSuperStaff, IsCustomer
from ec_base.common.constant.view_action import BaseViewAction
from ec_base.common.custom.pagination import CustomPagination
from ec_base.common.serializer.custom_mixins import CustomDestroyMixin
from ec_base.common.utils.exceptions import PermissionDenied
from ec_base.rating.models import Rating
from ec_staff.rating.filters.rating import RatingListQueryFields
from ec_staff.rating.serializers.rating import RatingListSlz, RatingRetrieveSlz, RatingCreateSlz, RatingUpdateSlz


class RatingViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    CustomDestroyMixin,
    GenericViewSet,
):
    permission_classes = (AllowAny,)
    pagination_class = CustomPagination
    filter_backends = (
        DjangoFilterBackend,
        OrderingFilter,
        SearchFilter,
    )
    serializer_class = RatingListSlz
    queryset = Rating.objects.all()
    filterset_fields = RatingListQueryFields.FILTERSET_FIELDS

    def get_serializer_class(self):
        slz_switcher = {
            BaseViewAction.LIST: RatingListSlz,
            BaseViewAction.RETRIEVE: RatingRetrieveSlz,
            BaseViewAction.CREATE: RatingCreateSlz,
            BaseViewAction.UPDATE: RatingUpdateSlz,
        }
        return slz_switcher.get(self.action, RatingListSlz)

    def get_permissions(self):
        perm_switcher = {
            BaseViewAction.LIST: (AllowAny,),
            BaseViewAction.RETRIEVE: (AllowAny,),
            BaseViewAction.CREATE: (IsCustomer,),
            BaseViewAction.UPDATE: (IsCustomer,),
            BaseViewAction.DESTROY: (IsManager | IsSuperStaff,),
        }
        self.permission_classes = perm_switcher.get(self.action)
        if self.permission_classes is None:
            raise PermissionDenied()

        return super().get_permissions()
