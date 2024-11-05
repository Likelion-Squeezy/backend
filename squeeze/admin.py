from django.contrib import admin
from .models import Squeeze

# Register your models here.
@admin.register(Squeeze)
class SqueezeAdmin(admin.ModelAdmin):
    list_display = ['title', 'user']