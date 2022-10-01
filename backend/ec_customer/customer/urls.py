from django.urls import path

from ec_base.common.constant.view_action import BaseViewAction
from ec_customer.customer.views.viewset import CustomerViewSet

urlpatterns = [
    path("create", CustomerViewSet.as_view({"post": BaseViewAction.CREATE})),
    path("update", CustomerViewSet.as_view({"put": BaseViewAction.UPDATE})),
    path("<int:pk>/detail", CustomerViewSet.as_view({"get": BaseViewAction.RETRIEVE})),
]
