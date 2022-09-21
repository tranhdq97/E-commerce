from django.urls import path

from ec_base.common.constant.view_action import BaseViewAction
from ec_base.master.views.viewset import MasterViewSet

urlpatterns = [
    path("<str:master_name>/list", MasterViewSet.as_view({"get": BaseViewAction.LIST})),
    path("<str:master_name>/create", MasterViewSet.as_view({"post": BaseViewAction.CREATE})),
    path("<str:master_name>/<int:id>/delete", MasterViewSet.as_view({"delete": BaseViewAction.DESTROY})),
]
