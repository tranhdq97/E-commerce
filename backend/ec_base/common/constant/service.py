from .db_table import DBTable
from ..utils.utils import BaseEnum


class Master(BaseEnum):
    # table_name, model_name, allowed_to_create
    m_city = DBTable.MASTER_CITY, 'MasterCity', True
    m_district = DBTable.MASTER_DISTRICT, 'MasterDistrict', False

    @staticmethod
    def list(allowed_to_create=False):
        master_list = list(filter(lambda c: (allowed_to_create is False or c.value[2]), Master))
        return [x.value[0].value for x in master_list]

    @staticmethod
    def unpack(master_name):
        master = list(filter(lambda c: c.value[0] == master_name, Master))
        if len(master) == 0:
            raise ValueError('Master does not exist.')

        return master[0].value
