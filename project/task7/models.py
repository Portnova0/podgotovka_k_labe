from django.db import models
class School(models.Model):
    name = models.CharField(max_length=30)
    director = models.OneToOneField('Director', on_delete=models.SET_NULL, null='School')
    def __str__(self):
        return self.name
class Director(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
# Create your models here.
