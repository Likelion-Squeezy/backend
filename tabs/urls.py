from django.urls import path
from . import views

urlpatterns = [
    path('', views.TabView.as_view())   
]