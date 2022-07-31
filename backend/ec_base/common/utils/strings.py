import re


def check_regex(pattern, input_string):
    return re.match(pattern, input_string)


def str2bool(input_string):
    return str(input_string).lower() in ('yes', 'true', 't', '1')
