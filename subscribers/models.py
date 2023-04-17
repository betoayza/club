from django.db import models

# Models es una clase base para crear modelos
# tiene muchas funcionalidades para tal fin

# Create your models here.


class Subscriber(models.Model):
    name = models.CharField(max_length=35)
    lastname = models.CharField(max_length=35)
