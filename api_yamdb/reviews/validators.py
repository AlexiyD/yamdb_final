import datetime

from django.core.exceptions import ValidationError


def validate_year(value):
    year = datetime.date.today().year
    if year <= value:
        raise ValidationError('Проверьте год выпуска!')
