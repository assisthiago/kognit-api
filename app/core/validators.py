import re

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def cpf_validator(value):
    if len(value) < 11:
        raise ValidationError(
            _('Ensure this field has 11 characters.'),
            params={'value': value},
        )

    if not re.search(r'\d{11}', value):
        raise ValidationError(
            _('Ensure this field has only digits.'),
            params={'value': value},
        )


class WalletQueryParamsValidator:
    def __init__(self, query_params):
        self.user = query_params.get('user')
        self.errors = []

    def is_valid(self):
        """Validates the query params sent from request.

        : return bool
        """
        if not self.user:
            self.errors.append({'user': 'This field may not be blank.'})

        if not self.__is_user_and_id():
            self.errors.append({'user': 'Invalid ID'})

        if self.errors:
            return False

        return True
    def __is_user_and_id(self):
        """Checks if is int.

        : return bool
        """
        try:
            self.bank = int(self.bank)
            return True
        except:
            return False
