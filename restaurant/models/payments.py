from django.db import models
import uuid
from . import Orders

class Payments(models.Model):
    id_payment = models.UUIDField(primary_key=True, default = uuid.uuid4, editable=False)
    id_order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    payment_amount = models.FloatField()
    date_payment = models.DateTimeField( auto_now_add=True)