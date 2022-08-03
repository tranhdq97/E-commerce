import re
from datetime import datetime


def check_regex(pattern, input_string):
    return re.match(pattern, input_string)


def str2bool(input_string):
    return str(input_string).lower() in ('yes', 'true', 't', '1')


def get_file_field_directory(instance, filename):
    return f'{instance.type_id}/{"staff" if instance.created_by.is_staff else "customer"}/{instance.created_by_id}/' + \
           f'{datetime.today().strftime("%Y/%m/%d")}/{filename}'
