from django.db import models
from .category import Category
import uuid

class Product(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    fantasyName = models.CharField(max_lenght=30)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    description = models.CharField(max_lenght=100)
    price = models.DecimalField()
    available2 = models.BooleanField()

    def __str__(self):
        return self.fantasyName