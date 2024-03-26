from django.db import models
import uuid

class Orders(models.Model):
    id_order = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # id_reservation = models.ForeignKey()
    status = models.CharField(max_length=12)
    order_time = models.DateTimeField( auto_now_add=True)
    
    def __str__(self):
        return self.status