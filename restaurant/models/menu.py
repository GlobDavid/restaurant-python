from django.db import models

# Model MENU
class Menu(models.Model):
    id_menu = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length = 20, null=False)
    description = models.CharField(max_length = 30)
    
    def __str__(self):
        return self.title
    