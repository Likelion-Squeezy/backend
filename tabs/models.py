from django.db import models

# Create your models here.
class Tab(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField(null=True, blank=True)
    favicon = models.URLField(null=True, blank=True)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title