from django.apps import apps
from django.db import IntegrityError
from django.shortcuts import get_object_or_404

from ..serializers.base_master import BaseMasterListSerializer, BaseMasterCreateSerializer, BaseMasterDetailSerializer
from ..serializers.district import DistrictListSerializer
from ...common.constant.app_label import ModelAppLabel
from ...common.constant.db_table import DBTable
from ...common.constant.service import Master


class BaseMasterService:
    def __init__(self, master_name):
        self.master_name = master_name
        self.table_name, self.model_name, self.allowed_to_create = getattr(Master, master_name)
        self.app_label = ModelAppLabel.MASTER
        self.model = apps.get_model(self.app_label, self.model_name)

    def get_item_by_id(self, pk):
        return get_object_or_404(self.model, pk=pk)

    def list(self, parent_id=None):
        queryset = self.model.objects.all().filter()
        if self.master_name == DBTable.MASTER_DISTRICT and parent_id is not None:
            return queryset.filter(city_id=parent_id)

        return queryset

    def create(self, data):
        try:
            serializer_class = self.get_master_create_serializer()
            serializer = serializer_class(data=data)
            serializer.is_valid(raise_exception=True)
            instances = self.model.objects.filter(**serializer.validated_data)
            if len(instances) > 0:
                instance = instances.first()
                instance.is_deleted = False
                instance.save()
            else:
                instance = self.model.objects.create(**serializer.validated_data)

            serializer = BaseMasterDetailSerializer(instance)
            return serializer
        except IntegrityError:
            raise ValueError("Duplicate item")

    def delete(self, pk):
        instance = self.get_item_by_id(pk)
        instance.is_deleted = True
        instance.save()

    def get_master_list_serializer(self, *args, **kwargs):
        if self.master_name == DBTable.MASTER_DISTRICT:
            return DistrictListSerializer(*args, **kwargs)

        return BaseMasterListSerializer(*args, **kwargs)

    @staticmethod
    def get_master_create_serializer():
        return BaseMasterCreateSerializer
