from django.db import models
from .category import Category
import uuid

class Product(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    fantasyName = models.CharField(max_length=30)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField()

    def __str__(self):
        return self.fantasyName