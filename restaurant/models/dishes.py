from django.db import models
import uuid
from . import Menu

class Dishes(models.Model):
    id_dish = models.UUIDField( primary_key = True, default = uuid.uuid4, editable = False)
    id_menus = models.ManyToManyField(Menu, related_name='menu')
    name = models.CharField(max_length=20, null=False)
    description = models.CharField(max_length=100, null=False)
    price = models.FloatField()
    available = models.BooleanField()
    
    def __str__(self):
        return self.name