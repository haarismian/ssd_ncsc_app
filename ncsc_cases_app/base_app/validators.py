# validators.py

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _

# Validator for max password length based on comment by Douglas Millward


class MaxLengthValidator:
    def __init__(self, max_length=20):
        self.max_length = max_length

    def validate(self, password, user=None):
        if len(password) > self.max_length:
            raise ValidationError(
                _("This password is too long. It must contain no more than %(max_length)d characters."),
                code='password_too_long',
                params={'max_length': self.max_length},
            )

    def get_help_text(self):
        return _(
            "Your password must contain no more than %(max_length)d characters."
        ) % {'max_length': self.max_length}
