from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):
	name = models.CharField(max_length=200)

	def __str__(self):
		return self.name

class Suggestion(models.Model):
	host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
	topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
	name= models.CharField(max_length=100)
	description = models.TextField(blank=True, null=True)
	updated = models.DateTimeField(auto_now=True)
	created = models.DateTimeField(auto_now_add=True)
	image = models.ImageField('upload-to')

	class Meta:
		ordering = ['-updated', '-created']


	verbose_name = 'Suggestions'

	def __str__(self):
		return self.name

