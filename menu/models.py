from django.db import models

# Create your models here.

class MenuItem(models.Model):
    restaurant_name = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()

    def __str__(self):
        return self.name
