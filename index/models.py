from django.db import models

# Create your models here.

class View(models.Model):
    number = models.IntegerField()
    
    def __str__(self):
        return f"{self.number}"
        
    class Meta:
        pass