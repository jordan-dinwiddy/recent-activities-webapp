from django.db import models
from django.forms import ModelForm
from activities import custom_validators

ACTIVITY_CHOICES = (
    ('RUNNING', 'Running'),
    ('CYCLING', 'Cycling'),
    ('SWIMMING', 'Swimming'),
    ('ROWING', 'Rowing'),
)

class Activity(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=20, choices=ACTIVITY_CHOICES, default='RUNNING')
    date = models.DateField(validators=[custom_validators.date_not_in_future])
    desc = models.TextField()

    # Text description of this model used by Django
    def __unicode__(self):
        return self.name

class ActivityForm(ModelForm):
    class Meta:
        model = Activity

