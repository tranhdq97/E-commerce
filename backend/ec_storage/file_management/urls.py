from django.urls import path

from ec_base.common.constant.view_action import BaseViewAction
from ec_storage.file_management.views.viewset import FileManagementViewSet

urlpatterns = [
    path("create", FileManagementViewSet.as_view({"post": BaseViewAction.CREATE})),
    path("list", FileManagementViewSet.as_view({"get": BaseViewAction.LIST})),
    path("<int:pk>/detail", FileManagementViewSet.as_view({"get": BaseViewAction.RETRIEVE})),
    path("<int:pk>/delete", FileManagementViewSet.as_view({"delete": BaseViewAction.DESTROY})),
    path("<int:pk>/update", FileManagementViewSet.as_view({"put": BaseViewAction.UPDATE})),
]
