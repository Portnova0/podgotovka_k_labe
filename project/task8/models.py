from django.db import models
class Device(models.Model):
    name = models.CharField(max_length=30)
    serailnumber = models.OneToOneField('SerialNumber',on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self):
        return self.name
class SerialNumber(models.Model):
    number = models.PositiveIntegerField(default=0)


# Create your models here.
