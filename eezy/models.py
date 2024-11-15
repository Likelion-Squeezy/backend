from django.db import models

# Create your models here.
class Eezy(models.Model):
    title = models.CharField(max_length=100)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, null=True, blank=True) 
    content = models.TextField()
    tab = models.ForeignKey('tabs.Tab', on_delete=models.CASCADE, related_name='eezies')
    created_at = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.title