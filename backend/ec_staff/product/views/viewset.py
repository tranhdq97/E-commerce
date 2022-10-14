from django.db import IntegrityError
from django.db.models import Avg
from django.db.models.functions import Round
from django_filters.rest_framework.backends import DjangoFilterBackend
from rest_framework import mixins
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from ec_base.auth.permissions.permission import IsSuperStaff, IsManager
from ec_base.common.constant import message
from ec_base.common.constant.view_action import BaseViewAction
from ec_base.common.custom.pagination import CustomPagination
from ec_base.common.serializer.custom_mixins import CustomDestroyMixin
from ec_base.common.utils.exceptions import PermissionDenied, APIErr
from ec_base.product.models import Product
from ec_staff.product.filters.product import ProductListQueryFields
from ec_staff.product.serializers.product import ProductListSlz, ProductRetrieveSlz, ProductCreateSlz, ProductUpdateSlz


class ProductViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    CustomDestroyMixin,
    GenericViewSet,
):
    permission_classes = (AllowAny,)
    pagination_class = CustomPagination
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    serializer_class = ProductListSlz
    queryset = Product.objects.all()
    search_fields = ProductListQueryFields.SEARCH_FIELDS
    ordering_fields = ProductListQueryFields.ORDER_FIELDS
    ordering = ProductListQueryFields.ORDER_DEFAULT_FIELD
    filterset_fields = ProductListQueryFields.FILTERSET_FIELDS

    def get_queryset(self):
        queryset = Product.objects.all().prefetch_related("rating").annotate(num_stars=Round(Avg("rating__num_stars")))
        return queryset

    def get_serializer_class(self):
        slz_switcher = {
            BaseViewAction.LIST: ProductListSlz,
            BaseViewAction.RETRIEVE: ProductRetrieveSlz,
            BaseViewAction.CREATE: ProductCreateSlz,
            BaseViewAction.UPDATE: ProductUpdateSlz,
        }
        slz = slz_switcher.get(self.action, ProductListSlz)
        return slz

    def get_permissions(self):
        perm_switcher = {
            BaseViewAction.LIST: (AllowAny,),
            BaseViewAction.RETRIEVE: (AllowAny,),
            BaseViewAction.CREATE: (IsManager | IsSuperStaff,),
            BaseViewAction.UPDATE: (IsManager | IsSuperStaff,),
            BaseViewAction.DESTROY: (IsManager | IsSuperStaff,),
        }
        self.permission_classes = perm_switcher.get(self.action)
        if self.permission_classes is None:
            raise PermissionDenied()

        return super().get_permissions()

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except IntegrityError:
            raise APIErr(detail=message.ALREADY_EXISTS)
