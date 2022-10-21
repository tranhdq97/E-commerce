class RegexPattern:
    PASSWORD = "^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).{8,255}$"
    SNAKE_CASE = "(?<!^)(?=[A-Z])"
    PHONE_NUMBER_REGEX = "^[0-9]{8,11}$"


class DateTimeFormat:
    TIMEZONE_OFFSET = 'TimezoneOffset'
    DEFAULT = "%Y-%m-%d %H:%M:%S"
    HOUR = "%Hh"
    DATE = "%d"
    MONTH = "%B"
    YEAR = "%Y"


class OverView:
    TIMESTAMPS = 'timestamps'
    DATASETS = 'datasets'
    NAME = 'name'
