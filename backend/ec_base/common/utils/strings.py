import hashlib
import os.path
import re
from datetime import datetime
from functools import partial


def check_regex(pattern, input_string):
    return re.match(pattern, input_string)


def str2bool(input_string):
    return str(input_string).lower() in ("yes", "true", "t", "1")


def hash_file(file, block_size=65536):
    hasher = hashlib.md5()
    for buf in iter(partial(file.read, block_size), b""):
        hasher.update(buf)

    return hasher.hexdigest()


def get_file_field_directory(instance, filename):
    instance.file.open()
    filename_base, filename_ext = os.path.splitext(filename)
    return f'{instance.type_id}/{datetime.today().strftime("%Y/%m/%d")}/{filename_base}{filename_ext}'
