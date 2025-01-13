from django.db import models
class Athlete(models.Model):
    name = models.CharField(max_length=50)
    nationalrecord = models.OneToOneField('NationalRecord', on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self):
        return self.name
class NationalRecord(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
# Create your models here.
