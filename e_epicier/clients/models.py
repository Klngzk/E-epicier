from django.db import models
from django.contrib.auth.models import User

class Client(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    cin = models.CharField(max_length=10)
    numero = models.CharField(max_length=15)
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    def __str__(self):
        return self.firstname