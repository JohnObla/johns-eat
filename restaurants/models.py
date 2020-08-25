from django.db import models
from django.contrib.auth import get_user_model


class Restaurant(models.Model):
    owner = models.ManyToManyField(get_user_model())

    name = models.CharField(
        "Name",
        max_length=200,
        help_text='Enter the restaurant name',
    )
    description = models.TextField(default='')

    address1 = models.CharField(
        "Address line 1",
        max_length=1024,
        default='',
    )
    address2 = models.CharField(
        "Address line 2",
        max_length=1024,
        default='',
        blank=True,
    )

    address3 = models.CharField(
        "Address line 3",
        max_length=1024,
        default='',
        blank=True,
    )

    zip_code = models.CharField(
        "ZIP / Postal code",
        max_length=12,
        default='',
    )

    city = models.CharField(
        "City",
        max_length=1024,
        default='',
    )

    country = models.CharField(
        "Country",
        max_length=1024,
        default='',
    )

    def __str__(self):
        return self.name


class Cuisine(models.Model):
    restaurant = models.ManyToManyField(Restaurant)

    name = models.CharField(
        "Name",
        max_length=200,
        help_text='Enter the cuisine name',
    )

    def __str__(self):
        return self.name


class Food(models.Model):
    restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name_plural = "food"

    name = models.CharField(
        "Name",
        max_length=200,
        help_text='Enter the food name',
    )
    description = models.TextField(blank=True)
    price = models.DecimalField(
        "Price",
        max_digits=5,
        decimal_places=2,
    )

    def __str__(self):
        return self.name


class Allergy(models.Model):
    food = models.ForeignKey(
        Food,
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name_plural = "allergies"

    name = models.CharField(
        "Name",
        max_length=200,
        help_text='Enter the allergy name',
    )

    def __str__(self):
        return self.name


class Category(models.Model):
    food = models.ManyToManyField(Food)

    class Meta:
        verbose_name_plural = "categories"

    name = models.CharField(
        "Name",
        max_length=200,
        help_text='Enter the category name',
    )

    def __str__(self):
        return self.name
