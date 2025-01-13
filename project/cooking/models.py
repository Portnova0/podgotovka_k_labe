from django.db import models
class Recipe(models.Model):
    name = models.CharField(max_length=30)
    instructions = models.ManyToManyField('Instructions')
    def __str__(self):
        return self.name
class Instructions(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name
# Create your models here.
