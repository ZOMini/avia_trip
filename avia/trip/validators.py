from django.core.exceptions import ValidationError
from django.utils import timezone


def validator_datetime(val):
    current = timezone.now()
    if val < current:
        raise ValidationError('Дата и время раньше текущей.')
