from django.db import models
import uuid
from . import Orders, Dishes

class Order_detail(models.Model):
    id_details = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    id_dish = models.ForeignKey(Dishes, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.FloatField()
    
    def __str__(self) -> str:
        return super().__str__()