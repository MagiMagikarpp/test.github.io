from django.db import models

# Create your models here.

class Item(models.Model):
    picture = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=0)
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name