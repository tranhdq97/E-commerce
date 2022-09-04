from ec_base.settings import *

ROOT_URLCONF = 'ec_customer.urls'

WSGI_APPLICATION = 'ec_customer.wsgi.application'

# ---------------------------------------------------------------------------- #
#                                 SWAGGER                                      #
# ---------------------------------------------------------------------------- #
SPECTACULAR_SETTINGS['TITLE'] = 'EC Customer Api'

REST_FRAMEWORK['DEFAULT_PERMISSION_CLASSES'] = [
    'ec_base.auth.permissions.permission.IsCustomer'
]
