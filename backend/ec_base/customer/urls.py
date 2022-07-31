from django.urls import path

from .views.viewset import CustomerViewSet
from ..common.constant.view_action import BaseViewAction

urlpatterns = [
    path('customer/list', CustomerViewSet.as_view({'get': BaseViewAction.LIST})),
    path('customer/create', CustomerViewSet.as_view({'post': BaseViewAction.CREATE})),
    path('customer/<int:pk>/update', CustomerViewSet.as_view({'put': BaseViewAction.UPDATE})),
    path('customer/<int:pk>/detail', CustomerViewSet.as_view({'get': BaseViewAction.RETRIEVE})),
]
