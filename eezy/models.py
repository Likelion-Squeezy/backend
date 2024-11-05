from django.db import models

# Create your models here.
class Eezy(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    tab = models.ForeignKey('tabs.Tab', on_delete=models.CASCADE)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title