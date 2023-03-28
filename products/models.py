from django.db import models

# Create your models here.
from django.db import models

class Product(models.Model):

    name = models.CharField(max_length=255)
    description =  models.TextField()
    created  = models.DateTimeField(auto_now_add=True)
    vendor = models.CharField(max_length=255)
    price = models.IntegerField()

    def __str__(self) ->str:
        return self.name 