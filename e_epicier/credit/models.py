from django.db import models
from produits.models import Produit 
from clients.models import Client 
from django.contrib.auth.models import User

# Create your models here.



class Credit(models.Model):
    titre = models.CharField(max_length=50)
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    date = models.DateField(auto_now_add=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE,default=1)
    to_pay =models.DecimalField(max_digits=9, decimal_places=2,default=0)
    payed = models.DecimalField(max_digits=9, decimal_places=2,default=0)
    etat = models.BooleanField(default=False)



class Qnt_Produit(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE,default=1)
    credit = models.ForeignKey(Credit,on_delete=models.CASCADE,default=1)
    qnt = models.PositiveIntegerField()
    date = models.DateField(auto_now_add=True)
    total = models.DecimalField(max_digits=9, decimal_places=2)