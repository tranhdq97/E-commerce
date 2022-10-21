from calendar import monthrange
from datetime import datetime, timedelta, timezone

from django.db.models import Q, Sum, F, OuterRef, Subquery

from ec_base.common.constant import message
from ec_base.common.constant.constant import DateTimeFormat, OverView
from ec_base.common.constant.db_fields import OrderItemFields, ProductFields, MasterProductCategoryFields
from ec_base.common.constant.master import MasterFilterByID
from ec_base.common.utils.exceptions import APIErr
from ec_base.common.utils.utils import get_timedelta, localize_time
from ec_base.master.models import MasterFilterBy, MasterProductCategory
from ec_base.order_item.models import OrderItem


class ProductCategorySvc:
    @staticmethod
    def _get_overview_conditions(filter_by_id, time_delta):
        if not MasterFilterBy.objects.filter(id=filter_by_id).exists():
            raise APIErr(detail=message.INVALID_INPUT)

        today = datetime.utcnow() + time_delta
        filter_by_switcher = {
            MasterFilterByID.TODAY: (
                DateTimeFormat.HOUR,
                [(
                    datetime(today.year, today.month, today.day, hour, 0, 0) - time_delta,
                    datetime(today.year, today.month, today.day, hour, 0, 0) + timedelta(hours=1) - time_delta,
                ) for hour in range(0, today.hour + 1)]
            ),
            MasterFilterByID.THIS_YEAR: (
                DateTimeFormat.MONTH,
                [(
                    datetime(today.year, month, 1, 0, 0, 0) - time_delta,
                    datetime(today.year, month, 1, 0, 0, 0) + timedelta(
                        days=monthrange(today.year, month)[-1]
                    ) - time_delta,
                ) for month in range(1, today.month + 1)]
            ),
            MasterFilterByID.LAST_FIVE_YEARS: (
                DateTimeFormat.YEAR,
                [(
                    datetime(year, 1, 1, 0, 0, 0) - time_delta,
                    datetime(year + 1, 1, 1, 0, 0, 0) - time_delta,
                ) for year in range(today.year - 4, today.year + 1)]
            ),
            MasterFilterByID.THIS_MONTH: (
                DateTimeFormat.DATE,
                [(
                    datetime(today.year, today.month, day, 0, 0, 0) - time_delta,
                    datetime(today.year, today.month, day, 0, 0, 0) + timedelta(days=1) - time_delta,
                ) for day in range(1, today.day + 1)]
            )
        }
        datetime_format, timestamps = filter_by_switcher.get(filter_by_id, MasterFilterByID.TODAY)
        timestamps = [[timestamp.astimezone(timezone.utc) for timestamp in ts_set] for ts_set in timestamps]
        return datetime_format, timestamps

    @staticmethod
    def _get_single_overview_condition(timestamp):
        return Q(Q(order__created_at__gte=timestamp[0]) & Q(order__created_at__lt=timestamp[1]))

    def _get_sale_quantity_by_datetime(self, timestamp):
        return MasterProductCategory.objects.annotate(
            quantity=Subquery(
                OrderItem.objects.filter(
                    Q(product__category=OuterRef('pk')) & self._get_single_overview_condition(timestamp)
                ).values(
                    "__".join([OrderItemFields.PRODUCT, ProductFields.CATEGORY_ID])
                ).annotate(
                    total_quantity=Sum(OrderItemFields.QUANTITY)
                ).values(OrderItemFields.TOTAL_QUANTITY)
            )
        ).values()

    def _get_sale_amount_by_datetime(self, timestamp):
        return MasterProductCategory.objects.annotate(
            amount=Subquery(
                OrderItem.objects.filter(
                    Q(product__category=OuterRef('pk')) & self._get_single_overview_condition(timestamp)
                ).values(
                    "__".join([OrderItemFields.PRODUCT, ProductFields.CATEGORY_ID])
                ).annotate(
                    total_amount=Sum(
                        F(OrderItemFields.QUANTITY) * F("__".join([OrderItemFields.PRODUCT, ProductFields.PRICE]))
                    ),
                ).values(OrderItemFields.TOTAL_AMOUNT)
            )
        ).values()

    def get_sale_quantity_overview(self, filter_by_id, slz_class, timezone_offset):
        time_delta = get_timedelta(timezone_offset)
        datetime_format, timestamps = self._get_overview_conditions(filter_by_id, time_delta)
        data = {OverView.TIMESTAMPS: [], OverView.DATASETS: []}
        for i, timestamp in enumerate(timestamps):
            slz_data = slz_class(self._get_sale_quantity_by_datetime(timestamp), many=True).data
            for j, category_data in enumerate(slz_data):
                if i == 0:
                    data[OverView.DATASETS].append(category_data.copy())
                    data[OverView.DATASETS][j][MasterProductCategoryFields.QUANTITY] = []

                data[OverView.DATASETS][j][MasterProductCategoryFields.QUANTITY].append(
                    category_data[MasterProductCategoryFields.QUANTITY] if category_data[
                        MasterProductCategoryFields.QUANTITY] else 0
                )

            data[OverView.TIMESTAMPS].append(localize_time(timestamp[0], time_delta).strftime(datetime_format))

        return data

    def get_sale_amount_overview(self, filter_by_id, slz_class, timezone_offset):
        time_delta = get_timedelta(timezone_offset)
        datetime_format, timestamps = self._get_overview_conditions(filter_by_id, time_delta)
        data = {OverView.TIMESTAMPS: [], OverView.DATASETS: []}
        for i, timestamp in enumerate(timestamps):
            slz_data = slz_class(self._get_sale_amount_by_datetime(timestamp), many=True).data
            for j, category_data in enumerate(slz_data):
                if i == 0:
                    data[OverView.DATASETS].append(category_data.copy())
                    data[OverView.DATASETS][j][MasterProductCategoryFields.AMOUNT] = []

                data[OverView.DATASETS][j][MasterProductCategoryFields.AMOUNT].append(
                    category_data[MasterProductCategoryFields.AMOUNT] if category_data[
                        MasterProductCategoryFields.AMOUNT] else 0
                )

            data[OverView.TIMESTAMPS].append(localize_time(timestamp[0], time_delta).strftime(datetime_format))

        return data
