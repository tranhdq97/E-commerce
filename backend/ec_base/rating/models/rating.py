from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from ec_base.common.constant.app_label import ModelAppLabel
from ec_base.common.constant.db_table import DBTable
from ec_base.common.models.base import Creator, Editor, DateTimeModel
from ec_base.file_management.models import FileManagement
from ec_base.product.models import Product


class Rating(Creator, Editor, DateTimeModel):
    comment = models.TextField()
    num_stars = models.IntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(5)])
    media = models.ForeignKey(to=FileManagement, on_delete=models.RESTRICT, null=True, related_name=DBTable.RATING)
    product = models.ForeignKey(to=Product, on_delete=models.RESTRICT, related_name=DBTable.RATING)

    class Meta:
        db_table = DBTable.RATING
        app_label = ModelAppLabel.RATING
