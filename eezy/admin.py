from django.contrib import admin
from .models import Eezy

# Register your models here.
@admin.register(Eezy)
class EezyAdmin(admin.ModelAdmin):
    list_display = ['title', 'tab', 'tab__user']