from django.db import models
from django.forms import ModelForm

class Activity(models.Model):
	name = models.CharField(max_length=100)
	type = models.CharField(max_length=100)
	date = models.DateTimeField()
	desc = models.CharField(max_length=500)

	# Text description of this model used by Django
	def __unicode__(self):
		return self.name

class ActivityForm(ModelForm):
	class Meta:
		model = Activity

