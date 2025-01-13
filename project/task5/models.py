from django.db import models
class Library(models.Model):
    name = models.CharField(max_length=30)
    book = models.ForeignKey('Book', on_delete=models.PROTECT)
class Book(models.Model):
    name = models.CharField(max_length=30)

# Create your models here.
