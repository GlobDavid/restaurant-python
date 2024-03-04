from enum import Enum
from django.db import models

# Create your models here.
class Category(models.Model):
    HAMBURGERS_AND_HOTDOGS = 1
    CHICKEN = 2
    FISH = 3
    MEATS = 4
    DESSERTS = 5
    VEGAN_FOOD = 6
    KIDS_MEALS = 7

    CHOICES = (
        (HAMBURGERS_AND_HOTDOGS, 'Hamburgers and Hotdogs'),
        (CHICKEN, 'Chicken'),
        (FISH, 'Fish'),
        (MEATS, 'Meats'),
        (DESSERTS, 'Desserts'),
        (VEGAN_FOOD, 'Vegan Food'),
        (KIDS_MEALS, 'Kids Meals'),
    )

    name = models.CharField(max_length=50, choices=CHOICES)

    def __str__(self):
        return self.get_name_display()