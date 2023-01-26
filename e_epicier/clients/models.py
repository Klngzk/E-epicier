from django.db import models

class Client(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    cin = models.CharField(max_length=10)
    numero = models.CharField(max_length=15)
