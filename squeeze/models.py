from django.db import models

# Create your models here.
class Squeeze(models.Model):
    title = models.CharField(max_length=100)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE) 
    tabs = models.ManyToManyField('tabs.Tab')
    image = models.ImageField(upload_to='images/')  
    created_at = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.title