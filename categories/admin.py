from django.contrib import admin
from .models import Category

# Register your models here.
@admin.register(Category)
class TabAdmin(admin.ModelAdmin):
    list_display = ('name', 'user') 