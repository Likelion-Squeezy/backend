from django.urls import path
from .views import EezyView

urlpatterns = [
    path('', EezyView.as_view()),
    path('<int:eezy_id>/', EezyView.as_view(), name='eezy-detail'),
]