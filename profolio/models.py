from django.db import models

# Create your models here.


class Profolio (models.Model):
    title = models.CharField(max_length=25)
    category = models.ForeignKey('category', related_name='category_project', on_delete=models.CASCADE)
    img = models.ImageField( upload_to="projet/")
     
    def __str__(self):
        return self.title
    
    
    class Meta :
         ordering = ["id"]
    
    
class category(models.Model):
    
    name =models.CharField( max_length=25)
    
    def __str__(self):
        return self.name
                    
    class Meta :
        
        verbose_name_plural = "categories"
        
    
    
    