from django.db import models

# Create your models here.
class Blog(models.Model):
    title =  models.CharField(max_length=150)
    description = models.TextField()


    def __str__(self) -> str:
        return self.title

class Contact(models.Model):
    name =  models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    message = models.TextField()


    def __str__(self) -> str:
        return self.name