from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.TextField()
    age = models.IntegerField()
    birth = models.DateField(auto_now=False, auto_now_add=False)
    nationality = models.TextField()

    def __str__(self):
        return self.name

class Book(models.Model):
    author = models.ForeignKey(Author, on_delete = models.CASCADE)
    title = models.TextField(max_length=100)
    description = models.TextField()
    adult = models.BooleanField()
    price = models.IntegerField()
