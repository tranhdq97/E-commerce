from django.urls import path

from .views.viewset import MasterViewSet
from ..common.constant.view_action import BaseViewAction

urlpatterns = [
    path('master/<master_name>/list', MasterViewSet.as_view({'get': BaseViewAction.LIST})),
    path('master/<master_name>/create', MasterViewSet.as_view({'post': BaseViewAction.CREATE})),
    path('master/<master_name>/<int:id>/delete', MasterViewSet.as_view({'delete': BaseViewAction.DESTROY})),
]
