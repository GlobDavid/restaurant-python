from django.db import models
from restaurant.enums import CategoryEnum

class Product(models.Model):
    uuid = models.BinaryField(max_length=16)
    fantasyName = models.CharField(max_length=30)
    category = models.CharField(max_length=50, choices=[(choice.value, choice.name) for choice in CategoryEnum], default=CategoryEnum.HAMBURGERS_AND_HOTDOGS.value)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField()

    class Meta:
        db_table = 'products'

    def __str__(self):
        return self.fantasyName