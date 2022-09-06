from rest_framework import serializers

from ec_base.common.constant.db_fields import CommonFields, RatingFields
from ec_base.common.utils.serializer import ForeignKeyField
from ec_base.file_management.models import FileManagement
from ec_base.product.models import Product
from ec_base.rating.models import Rating


class BaseRatingSlz(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = (CommonFields.ID, RatingFields.PRODUCT_ID,)


class RatingCreateSlz(BaseRatingSlz):
    media_id = ForeignKeyField(model=FileManagement, required=False)
    product_id = ForeignKeyField(model=Product, required=False)

    class Meta:
        model = BaseRatingSlz.Meta.model
        fields = BaseRatingSlz.Meta.fields + (RatingFields.COMMENT, RatingFields.NUM_STARS, RatingFields.MEDIA_ID,)


class RatingUpdateSlz(BaseRatingSlz):
    media_id = ForeignKeyField(model=FileManagement, required=False)
    product_id = ForeignKeyField(model=Product, required=False)

    class Meta:
        model = BaseRatingSlz.Meta.model
        fields = BaseRatingSlz.Meta.fields + (
            RatingFields.COMMENT, RatingFields.NUM_STARS, RatingFields.MEDIA_ID,)


class RatingListSlz(BaseRatingSlz):
    class Meta:
        model = BaseRatingSlz.Meta.model
        fields = BaseRatingSlz.Meta.fields + (RatingFields.NUM_STARS, RatingFields.MEDIA_ID)


class RatingRetrieveSlz(BaseRatingSlz):
    class Meta:
        model = BaseRatingSlz.Meta.model
        fields = BaseRatingSlz.Meta.fields + (RatingFields.COMMENT, RatingFields.NUM_STARS, RatingFields.MEDIA_ID) + (
            CommonFields.CREATED_AT, CommonFields.CREATED_BY_ID, CommonFields.UPDATED_AT, CommonFields.UPDATED_BY_ID)
