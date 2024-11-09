from django.urls import path
from .views import SqueezeView

urlpatterns = [
    path('', SqueezeView.as_view()),
    path('<int:squeeze_id>/', SqueezeView.as_view(), name='squeeze-detail'),
]