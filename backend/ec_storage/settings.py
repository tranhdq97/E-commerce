from ec_base.settings import *

ROOT_URLCONF = "ec_storage.urls"

WSGI_APPLICATION = "ec_storage.wsgi.application"

# ---------------------------------------------------------------------------- #
#                                 SWAGGER                                      #
# ---------------------------------------------------------------------------- #
SPECTACULAR_SETTINGS["TITLE"] = "EC Storage Api"

REST_FRAMEWORK["DEFAULT_PERMISSION_CLASSES"] = ["rest_framework.permissions.IsAuthenticated"]
