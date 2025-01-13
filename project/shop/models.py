from django.db import models
class Order(models.Model):
    name = models.CharField(max_length=30)
    orderitem = models.ForeignKey('OrderItem', on_delete=models.CASCADE)
    def __str__(self):
        return self.name
class OrderItem(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name
# Create your models here.
