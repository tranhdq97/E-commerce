from django.utils.translation import gettext_lazy as _

MUST_HAVE_EMAIL = _('User must have an email address.')
PASSWORD_FAILED = _("At least one uppercase letter, one lowercase letter, one number")
PASSWORD_IDENTICAL_AS_EMAIL = _("The same string sequence as the email address")
PASSWORD_DID_NOT_MATCH = _("Dont match current password. Please check again")
PASSWORD_CHANGE_SUCCESSFUL = _("Change password successfully")
ALREADY_HAVE_SUPER_STAFF = _("There is no room for two super staff.")

NOT_EXIST = _('Does not exist')
NO_SERIALIZER_MATCHED = _("There is no serializer matched with this action")
DUPLICATE_ENTRY = _("Duplicate entry")

FILE_SIZE_EXCEED_LIMIT = _(
    'Please keep filesize under %(limit_value)sKB. Current filesize %(show_value)sKB')
NOT_SUPPORTED_FILE_TYPE = _('Filetype is not supported.')
NOT_MATCHED_FILE_TYPE = _('Filetype does not match the submitted file')

# Master
NOT_ALLOWED_TO_CREATE = _("This master is not allowed to create.")
