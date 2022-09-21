from django.urls import path

from ec_base.common.constant.view_action import BaseViewAction, OrderViewAction
from ec_customer.order.views.viewset import OrderViewSet

urlpatterns = [
    path("create", OrderViewSet.as_view({"post": BaseViewAction.CREATE})),
    path("list", OrderViewSet.as_view({"get": BaseViewAction.LIST})),
    path("<int:pk>/detail", OrderViewSet.as_view({"get": BaseViewAction.RETRIEVE})),
    path("<int:pk>/cancel", OrderViewSet.as_view({"put": OrderViewAction.CANCEL})),
]
