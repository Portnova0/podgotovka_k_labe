from django.db import models
class Chef(models.Model):
    name = models.CharField(max_length=30)
    recipe = models.ForeignKey('Recipe', on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.name
class Recipe(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
# Create your models here.
