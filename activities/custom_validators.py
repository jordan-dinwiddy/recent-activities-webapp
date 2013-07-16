import datetime
from django.core.exceptions import ValidationError

def date_not_in_future(date):
    """Custom validator to ensure a date is not in the future"""
    if date > datetime.date.today():
        raise ValidationError("You cannot select a date in the future")
