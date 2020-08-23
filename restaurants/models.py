from django.db import models


class Food(models.Model):
    name = models.CharField(max_length=200, help_text='Enter the name of food')
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name
