from rest_framework import serializers

from ..models import Product
from ...common.constant.db_fields import CommonFields, ProductFields, RatingFields
from ...common.utils.serializer import ForeignKeyField
from ...file_management.models import FileManagement
from ...master.models import MasterProductCategory
from ...master.serializers import BaseMasterListSlz
from ...master.serializers.base_master import BaseMasterRetrieveSlz


class BaseProductSlz(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (CommonFields.ID,)


class ProductCreateSlz(BaseProductSlz):
    category_id = ForeignKeyField(model=MasterProductCategory)
    photo_id = ForeignKeyField(model=FileManagement, required=False)

    class Meta:
        model = BaseProductSlz.Meta.model
        fields = BaseProductSlz.Meta.fields + (
            ProductFields.NAME, ProductFields.QUANTITY, ProductFields.PURCHASE_PRICE, ProductFields.PRICE,
            ProductFields.DESC, ProductFields.CATEGORY_ID, ProductFields.PHOTO_ID,
        )


class ProductUpdateSlz(BaseProductSlz):
    category_id = ForeignKeyField(model=MasterProductCategory)
    photo_id = ForeignKeyField(model=FileManagement, required=False)

    class Meta:
        model = BaseProductSlz.Meta.model
        fields = BaseProductSlz.Meta.fields + (
            ProductFields.NAME, ProductFields.QUANTITY, ProductFields.PURCHASE_PRICE, ProductFields.PRICE,
            ProductFields.DESC, ProductFields.CATEGORY_ID, ProductFields.PHOTO_ID)


class ProductListSlz(BaseProductSlz):
    category = BaseMasterListSlz(many=False)
    photo_id = ForeignKeyField(model=FileManagement, required=False)
    num_stars = serializers.FloatField()

    class Meta:
        model = BaseProductSlz.Meta.model
        fields = BaseProductSlz.Meta.fields + (
            ProductFields.NAME, ProductFields.QUANTITY, ProductFields.PRICE, ProductFields.CATEGORY,
            ProductFields.PHOTO_ID,) + (RatingFields.NUM_STARS,)


class ProductRetrieveSlz(BaseProductSlz):
    category = BaseMasterRetrieveSlz(many=False)
    photo_id = ForeignKeyField(model=FileManagement, required=False)
    num_stars = serializers.FloatField()

    class Meta:
        model = BaseProductSlz.Meta.model
        fields = BaseProductSlz.Meta.fields + (
            ProductFields.NAME, ProductFields.QUANTITY, ProductFields.PRICE, ProductFields.DESC,
            ProductFields.CATEGORY, ProductFields.PHOTO_ID,) + (RatingFields.NUM_STARS,)


class ProductRetrieveForStaffSlz(BaseProductSlz):
    category = BaseMasterRetrieveSlz(many=False)
    photo_id = ForeignKeyField(model=FileManagement, required=False)
    num_stars = serializers.FloatField()

    class Meta:
        model = BaseProductSlz.Meta.model
        fields = BaseProductSlz.Meta.fields + (
            ProductFields.NAME, ProductFields.QUANTITY, ProductFields.PRICE, ProductFields.PURCHASE_PRICE,
            ProductFields.DESC, ProductFields.CATEGORY, ProductFields.PHOTO_ID,) + (RatingFields.NUM_STARS,)
