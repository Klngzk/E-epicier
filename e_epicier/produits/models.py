from django.db import models

class Produit(models.Model):
    name = models.CharField(max_length=50)
    prix = models.DecimalField(max_digits=9, decimal_places=2)
