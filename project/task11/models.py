from django.db import models
class UserProfile(models.Model):
    user = models.CharField(max_length=30)

    def __str__(self):
        return self.user
class Address(models.Model):
    street = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

# Create your models here.
