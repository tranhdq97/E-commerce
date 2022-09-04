from ec_base.settings import *

ROOT_URLCONF = 'ec_staff.urls'

WSGI_APPLICATION = 'ec_staff.wsgi.application'

# ---------------------------------------------------------------------------- #
#                                 SWAGGER                                      #
# ---------------------------------------------------------------------------- #
SPECTACULAR_SETTINGS['TITLE'] = 'EC Staff Api'

REST_FRAMEWORK['DEFAULT_PERMISSION_CLASSES'] = [
    'ec_base.auth.permissions.permission.IsStaff'
]
