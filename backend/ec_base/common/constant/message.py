from django.utils.translation import gettext_lazy as _

PASSWORD_FAILED = _("At least one uppercase letter, one lowercase letter, one number")
PASSWORD_IDENTICAL_AS_EMAIL = _("The same string sequence as the email address")
PASSWORD_DID_NOT_MATCH = _("Dont match current password. Please check again")
PASSWORD_CHANGE_SUCCESSFUL = _("Change password successfully")

NO_SERIALIZER_MATCHED = _("There is no serializer matched with this action")
DUPLICATE_ENTRY = _("Duplicate entry")

FILE_SIZE_EXCEED_LIMIT = _('Please keep filesize under %(limit_value)s. Current filesize %(show_value)s')
NOT_SUPPORTED_FILE_TYPE = _('Filetype is not supported.')
NOT_MATCHED_FILE_TYPE = _('Filetype does not match the submitted file')
