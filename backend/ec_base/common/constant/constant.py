from ec_base.common.utils.utils import BaseEnum


class RegexPattern(str, BaseEnum):
    PASSWORD = "^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).{8,255}$"
    SNAKE_CASE = "(?<!^)(?=[A-Z])"
    PHONE_NUMBER_REGEX = "^[0-9]{8,11}$"
