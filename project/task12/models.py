from django.db import models
class User(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField()
    def __str__(self):
        return self.username
# Create your models here.
