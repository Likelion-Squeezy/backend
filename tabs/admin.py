from django.contrib import admin
from .models import Tab

# Register your models here.
@admin.register(Tab)
class TabAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'content', 'category')