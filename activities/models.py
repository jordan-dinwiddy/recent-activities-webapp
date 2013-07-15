from django.db import models
from django.forms import ModelForm
from django.core.exceptions import ValidationError
import datetime

ACTIVITY_CHOICES = (
    ('RUNNING', 'Running'),
    ('CYCLING', 'Cycling'),
    ('SWIMMING', 'Swimming'),
    ('ROWING', 'Rowing'),
)

def date_not_in_future(date):
    """Custom validator to ensure a date is not in the future"""
    if date > datetime.date.today():
    	raise ValidationError("You cannot select a date in the future")

class Activity(models.Model):
	name = models.CharField(max_length=100)
	type = models.CharField(max_length=20, choices=ACTIVITY_CHOICES)
	date = models.DateField(validators=[date_not_in_future])
	desc = models.TextField()

	# Text description of this model used by Django
	def __unicode__(self):
		return self.name

class ActivityForm(ModelForm):
	class Meta:
		model = Activity

