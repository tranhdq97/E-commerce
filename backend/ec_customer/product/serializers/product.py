from rest_framework import serializers

from ec_base.common.constant.db_fields import CommonFields, ProductFields, RatingFields
from ec_base.common.utils.serializer import ForeignKeyField
from ec_base.file_management.models import FileManagement
from ec_base.master.models import MasterProductCategory
from ec_base.master.serializers import BaseMasterListSlz
from ec_base.master.serializers.base_master import BaseMasterRetrieveSlz
from ec_base.product.models import Product


class ProductBaseSlz(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (CommonFields.ID,)


class ProductCreateSlz(ProductBaseSlz):
    category_id = ForeignKeyField(model=MasterProductCategory)
    photo_id = ForeignKeyField(model=FileManagement, required=False)

    class Meta:
        model = ProductBaseSlz.Meta.model
        fields = ProductBaseSlz.Meta.fields + (
            ProductFields.NAME,
            ProductFields.QUANTITY,
            ProductFields.PURCHASE_PRICE,
            ProductFields.PRICE,
            ProductFields.DESC,
            ProductFields.CATEGORY_ID,
            ProductFields.PHOTO_ID,
        )


class ProductUpdateSlz(ProductBaseSlz):
    category_id = ForeignKeyField(model=MasterProductCategory)
    photo_id = ForeignKeyField(model=FileManagement, required=False)

    class Meta:
        model = ProductBaseSlz.Meta.model
        fields = ProductBaseSlz.Meta.fields + (
            ProductFields.NAME,
            ProductFields.QUANTITY,
            ProductFields.PURCHASE_PRICE,
            ProductFields.PRICE,
            ProductFields.DESC,
            ProductFields.CATEGORY_ID,
            ProductFields.PHOTO_ID,
        )


class ProductListSlz(ProductBaseSlz):
    category = BaseMasterListSlz(many=False)
    num_stars = serializers.FloatField()

    class Meta:
        model = ProductBaseSlz.Meta.model
        fields = (
            ProductBaseSlz.Meta.fields
            + (
                ProductFields.NAME,
                ProductFields.QUANTITY,
                ProductFields.PRICE,
                ProductFields.CATEGORY,
                ProductFields.PHOTO_ID,
            )
            + (RatingFields.NUM_STARS,)
            + (CommonFields.CREATED_AT,)
        )


class ProductRetrieveSlz(ProductBaseSlz):
    category = BaseMasterRetrieveSlz(many=False)
    num_stars = serializers.FloatField()

    class Meta:
        model = ProductBaseSlz.Meta.model
        fields = (
            ProductBaseSlz.Meta.fields
            + (
                ProductFields.NAME,
                ProductFields.QUANTITY,
                ProductFields.PRICE,
                ProductFields.DESC,
                ProductFields.CATEGORY,
                ProductFields.PHOTO_ID,
            )
            + (RatingFields.NUM_STARS,)
        )


class ProductRetrieveForStaffSlz(ProductBaseSlz):
    category = BaseMasterRetrieveSlz(many=False)
    num_stars = serializers.FloatField()

    class Meta:
        model = ProductBaseSlz.Meta.model
        fields = (
            ProductBaseSlz.Meta.fields
            + (
                ProductFields.NAME,
                ProductFields.QUANTITY,
                ProductFields.PRICE,
                ProductFields.PURCHASE_PRICE,
                ProductFields.DESC,
                ProductFields.CATEGORY,
                ProductFields.PHOTO_ID,
            )
            + (RatingFields.NUM_STARS,)
        )


class ProductForOrderItemRetrieveSlz(ProductBaseSlz):
    class Meta:
        model = ProductBaseSlz.Meta.model
        fields = ProductBaseSlz.Meta.fields + (
            ProductFields.NAME,
            ProductFields.QUANTITY,
            ProductFields.PRICE,
            ProductFields.PHOTO_ID,
        )
