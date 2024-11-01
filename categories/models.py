from django.db import models

# Create your models here.
class Category(models.Model):
    # 여기에 model field들을 작성해주세요!
    name = models.CharField(max_length=50)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='categories')
