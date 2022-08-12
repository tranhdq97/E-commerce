from django.urls import path

from .views.viewset import FileManagementViewSet
from ..common.constant.view_action import BaseViewAction

urlpatterns = [
    path('create', FileManagementViewSet.as_view({'post': BaseViewAction.CREATE})),
    path('list', FileManagementViewSet.as_view({'get': BaseViewAction.LIST})),
    path('<int:pk>/detail', FileManagementViewSet.as_view({'get': BaseViewAction.RETRIEVE})),
    path('<int:pk>/delete', FileManagementViewSet.as_view({'delete': BaseViewAction.DESTROY})),
    path('<int:pk>/update', FileManagementViewSet.as_view({'put': BaseViewAction.UPDATE})),
]
