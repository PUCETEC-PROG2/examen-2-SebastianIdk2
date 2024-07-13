from django.db import models

# Create your models here.

class Movie (models.Model):
    title = models.CharField(max_length=50, null=False)
    gender = models.CharField(max_length=35, null=False)
    director = models.CharField(max_length=50, null=False)
    year = models.IntegerField(null=False)
    synopsis = models.TextField(max_length=300, null=False)
    
    def __str__(self) -> str:
        return self.title