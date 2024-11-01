from django.db import models

# Create your models here.
class Tab(models.Model):
    # 여기에 model field들을 작성해주세요!
    title = models.CharField(max_length=50)
    url = models.URLField()
    content = models.TextField()
    category = models.ForeignKey('categories.Category', on_delete=models.CASCADE, related_name='tabs')  