from django.core.exceptions import ValidationError


def positive_validator(value):
    if value < 0:
        raise ValidationError(
            f'{value} is not positive',
            params={'value': value}
        )
