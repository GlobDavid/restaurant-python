from django.db import models
import uuid

# Model MENU
class Menu(models.Model):
    id_menu = models.UUIDField( primary_key = True, default = uuid.uuid4, editable = False)
    title = models.CharField(max_length = 20, null=False)
    description = models.CharField(max_length = 30)
    
    def __str__(self):
        return self.title
    