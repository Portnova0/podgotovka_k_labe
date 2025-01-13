from django.db import models
class User(models.Model):
    username = models.CharField(max_length=30)
    def __str__(self):
        return self.username
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.user.username
# Create your models here.
