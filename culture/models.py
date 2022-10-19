from django.db import models

# Create your models here.

class Category(models.Model):
  '''category model'''
  name = models.CharField(max_length=100,null=False,blank=False)
  
  def __str__(self):
    return self.name
  
  
class Location(models.Model):
    '''location model'''
    name = models.CharField(max_length=100, null=False, blank=False)    
    
    def __str__(self):
        return self.name  

class Image(models.Model):
  '''image model'''
  name = models.CharField(max_length=25)
  image = models.ImageField(null=False,blank=False)
  description = models.CharField(max_length=500, null=False, blank=False)
  location = models.ForeignKey("Location", on_delete=models.SET_NULL, null=True)
  category = models.ForeignKey("Category", on_delete=models.SET_NULL , null=True )
    
    
   
    
    
