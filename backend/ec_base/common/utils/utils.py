import enum
from datetime import datetime, timedelta, timezone
from enum import Enum


@enum.unique
class BaseEnum(Enum):
    def __str__(self):
        return self.value


def get_timedelta(timezone_offset):
    return timedelta(hours=int(timezone_offset))


def get_timezone(time_delta: timedelta):
    return timezone(time_delta)


def localize_time(time: datetime, time_delta: timedelta):
    return time + time_delta
