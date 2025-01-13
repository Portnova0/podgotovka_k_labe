from django.db import models
class Book(models.Model):
    title = models.CharField(max_length=30)
    publication_date = models.DateField(auto_now_add=True)
    author = models.ManyToManyField('Author', related_name='author')
    genre = models.ManyToManyField('Genre', related_name='genre')
    def __str__(self):
        return self.title
class Author(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name
class Genre(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name
# Create your models here.
