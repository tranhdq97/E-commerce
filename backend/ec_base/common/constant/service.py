from .db_table import DBTable


class Master:
    # table_name, model_name, allowed_to_create
    m_city = DBTable.MASTER_CITY, 'MasterCity', True
    m_district = DBTable.MASTER_DISTRICT, 'MasterDistrict', True

    def __str__(self):
        return self.value()
