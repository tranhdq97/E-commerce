from ec_base.common.constant import message
from ec_base.common.constant.db_table import DBTable
from ec_base.common.utils.exceptions import APIErr
from ec_base.common.utils.utils import BaseEnum


class Master(BaseEnum):
    # table_name, model_name, allowed_to_create
    m_sex = DBTable.MASTER_SEX, "MasterSex", False
    m_city = DBTable.MASTER_CITY, "MasterCity", True
    m_district = DBTable.MASTER_DISTRICT, "MasterDistrict", False
    m_discount_rate = DBTable.MASTER_DISCOUNT_RATE, "MasterDiscountRate", False
    m_discount_type = DBTable.MASTER_DISCOUNT_TYPE, "MasterDiscountType", True
    m_file_type = DBTable.MASTER_FILE_TYPE, "MasterFileType", False
    m_order_status = DBTable.MASTER_ORDER_STATUS, "MasterOrderStatus", False
    m_payment_status = DBTable.MASTER_PAYMENT_STATUS, "MasterPaymentStatus", False
    m_shipping_status = DBTable.MASTER_SHIPPING_STATUS, "MasterShippingStatus", False
    m_customer_type = DBTable.MASTER_CUSTOMER_TYPE, "MasterCustomerType", False
    m_product_category = DBTable.MASTER_PRODUCT_CATEGORY, "MasterProductCategory", True
    m_filter_by = DBTable.MASTER_FILTER_BY, "MasterFilterBy", False

    @staticmethod
    def list(allowed_to_create=False):
        master_list = list(filter(lambda c: (allowed_to_create is False or c.value[2]), Master))
        return [x.value[0].value for x in master_list]

    @staticmethod
    def unpack(master_name):
        master = list(filter(lambda c: c.value[0] == master_name, Master))
        if len(master) == 0:
            raise APIErr(message.NOT_EXIST)

        return master[0].value
