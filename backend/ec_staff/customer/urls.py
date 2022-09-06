from django.urls import path

from ec_base.common.constant.view_action import BaseViewAction
from ec_staff.customer.views.viewset import CustomerViewSet

urlpatterns = [
    path('list', CustomerViewSet.as_view({'get': BaseViewAction.LIST})),
]
