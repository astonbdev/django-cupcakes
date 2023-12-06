from django.db import models


class Cupcake(models.Model):
    """Cupcake Model"""
    flavor = models.CharField(max_length=100)
    rating = models.IntegerField()
    size = models.TextField()
    image = models.TextField()
