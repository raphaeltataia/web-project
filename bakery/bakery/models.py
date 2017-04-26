from django.db import models
from django.utils import timezone

# Create your models here.

class Recipe(models.Model):
    chief = models.ForeignKey('Chief')
    title = models.CharField(max_length=200)
    ingredients = models.CharField(max_length=150)
    way = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    people_served = models.CharField(max_length=2)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Chief(models.Model):
	cpf = models.CharField(max_length=14, primary_key=True)
	name = models.CharField(max_length=30)
	city = models.CharField(max_length=25)
	state = models.CharField(max_length=2)
	email = models.EmailField(max_length=50)
	
	def __str__(self):
		return self.name