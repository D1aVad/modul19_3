from django.db import models

# Create your models here.

class Buyer(models.Model):
    username = models.CharField(max_length=30)
    password = models.IntegerField()
    age = models.IntegerField()

    def __str__(self):
        return self.username
    
class Game(models.Model):
    title = models.CharField(max_length=30)
    cost = models.DecimalField(decimal_places=2, max_digits=7)
    size = models.DecimalField(decimal_places=2, max_digits=8)
    description = models.TextField()
    age_limited = models.BooleanField(True)
    buyer = models.ManyToManyField(Buyer, related_name='buyer')
    

    def __str__(self):
        return self.title 