from unicodedata import name
from django.db import models
from django.contrib.auth.models import User

class DogToy(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=50)

    def __str__(self):
        return self.name

# Create your models here.
GENDER_CHOICES = {
    ("f", "female"),
    ("m", "male")
}

class Dog(models.Model):

    name = models.CharField(max_length=50)
    img = models.CharField(max_length=250)
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices = GENDER_CHOICES)
    breed = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE) #1:m
    dogtoys = models.ManyToManyField(DogToy) #m:m
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
