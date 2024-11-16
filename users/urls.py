from django.urls import path
from .views import UserView, RegisterView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
]