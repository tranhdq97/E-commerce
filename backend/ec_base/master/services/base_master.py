from django.apps import apps
from django.db import IntegrityError
from django.shortcuts import get_object_or_404

from ec_base.common.constant import message
from ec_base.common.constant.app_label import ModelAppLabel
from ec_base.common.constant.db_table import DBTable
from ec_base.common.constant.service import Master
from ec_base.common.utils.exceptions import APIErr
from ec_base.master.serializers.base_master import BaseMasterListSlz, BaseMasterRetrieveSlz, BaseMasterCreateSlz
from ec_base.master.serializers.discount_rate import MasterDiscountRateSlz
from ec_base.master.serializers.district import MasterDistrictSlz


class MasterBaseService:
    def __init__(self, master_name):
        self.master_name = master_name
        self.table_name, self.model_name, self.allowed_to_create = Master.unpack(master_name)
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

            serializer = BaseMasterRetrieveSlz(instance)
            return serializer
        except IntegrityError:
            raise APIErr(message.DUPLICATE_ENTRY)

    def delete(self, pk):
        instance = self.get_item_by_id(pk)
        instance.is_deleted = True
        instance.save()

    def get_master_list_serializer(self, *args, **kwargs):
        slz_switcher = {
            DBTable.MASTER_DISTRICT: MasterDistrictSlz,
            DBTable.MASTER_DISCOUNT_RATE: MasterDiscountRateSlz,
        }
        slz = slz_switcher.get(self.master_name, BaseMasterListSlz)
        return slz(*args, **kwargs)

    def get_master_create_serializer(self):
        if not self.allowed_to_create:
            raise APIErr(message.NOT_ALLOWED_TO_CREATE)

        return BaseMasterCreateSlz
