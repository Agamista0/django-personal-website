from django.db import models


# Create your models here.


class Services (models.Model):
    
    title = models.CharField(max_length=25)
    icon = models.CharField(max_length= 20)
    descritpion = models.TextField(max_length=100)
    
    def __str__(self):
        return self.title
    
    
    class Meta :
        
        ordering = ["-id"]
        
        
class Facts (models.Model):
    projects_completed =models.IntegerField(default=0)
    Clients =models.IntegerField(default=0)
    coffee =models.IntegerField(default=0)
    real_professional=models.IntegerField(default=0)
    
    def __str__(self):
        return str(self.id)
    