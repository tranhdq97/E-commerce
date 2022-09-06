from django.utils.translation import gettext_lazy as _

# Authentication
MUST_HAVE_EMAIL = _('User must have an email address.')
PASSWORD_FAILED = _("At least one uppercase letter, one lowercase letter, one number")
PASSWORD_IDENTICAL_AS_EMAIL = _("The same string sequence as the email address")
PASSWORD_DID_NOT_MATCH = _("Dont match current password. Please check again")
PASSWORD_CHANGE_SUCCESSFUL = _("Change password successfully")
ALREADY_HAVE_SUPER_STAFF = _("There is no room for two super staff.")
PROVIDE_MUST_BE_STAFF_OR_CUSTOMER = _("Provider must be staff or customer")
INVALID_PROVIDER = _("Invalid provider")
EMAIL_OR_PASSWORD_IS_INCORRECT = _("The email address or password is incorrect")
INVALID_TOKEN = _("Invalid token")

# Permission
PERMISSION_DENIED = 'permission denied'

# Query database
NOT_EXIST = _('Does not exist')
NO_SERIALIZER_MATCHED = _("There is no serializer matched with this action")
DUPLICATE_ENTRY = _("Duplicate entry")
FILE_SIZE_EXCEED_LIMIT = _(
    'Please keep filesize under %(limit_value)sKB. Current filesize %(show_value)sKB')
NOT_SUPPORTED_FILE_TYPE = _('Filetype is not supported.')
NOT_MATCHED_FILE_TYPE = _('Filetype does not match the submitted file')
INVALID_INPUT = 'Invalid input'
ALREADY_EXISTS = 'Already exists'

# Master
NOT_ALLOWED_TO_CREATE = _("This master is not allowed to create.")

# Other
PASSWORD_INAPPROPRIATE = _(
    "Password must contain 7 letters or greater, one digit from 0 to 9, one lowercase letter, one uppercase letter")
PASSWORD_MUST_DIFFER_EMAIL = _("Password must differ email address")
