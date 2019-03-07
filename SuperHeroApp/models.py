from django.db import models

# Create your models here.

# superhero model
class SuperHeroApp(models.Model):
    name = models.CharField(max_length=200, default="")
    cityorigin= models.CharField(max_length=200, default="")
    richpower = models.CharField(max_length=200, default="")
    whichPower = models.CharField(max_length=200, default="")
    goodEvil = models.CharField(max_length=200, default="")
    examples = models.TextField(max_length=50000000, default="")
