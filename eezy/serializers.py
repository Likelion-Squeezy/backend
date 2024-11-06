from rest_framework.serializers import ModelSerializer
from .models import Eezy
from tabs.models import Tab
from tabs.serializers import TabSerializer

class EezySerializer(ModelSerializer):
    class Meta:
        model = Eezy
        fields = ['id', 'title', 'content', 'tab']

        tab = TabSerializer(read_only=True)