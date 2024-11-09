from rest_framework import serializers
from .models import Squeeze
from tabs.serializers import TabSerializer

class SqueezeSerializer(serializers.ModelSerializer):
    tabs = TabSerializer(many=True, read_only=True)

    class Meta:
        model = Squeeze
        fields = ['id', 'title', 'tabs']