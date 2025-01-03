from django.urls import path
from .views import UserView, RegisterView, LoginView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path("login/", LoginView.as_view(), name='login'),
    path('profile/', UserView.as_view()),
]