from django.db import models
from django.contrib.auth.models import User

class Produit(models.Model):
    name = models.CharField(max_length=50)
    prix = models.DecimalField(max_digits=9, decimal_places=2)
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
