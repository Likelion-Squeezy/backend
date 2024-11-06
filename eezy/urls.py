from django.urls import path
from .views import EezyView

urlpatterns = [
    path('', EezyView.as_view())
]