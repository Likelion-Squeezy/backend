from rest_framework import serializers
from .models import Squeeze
from tabs.serializers import TabSerializer
from tabs.models import Tab

class SqueezeSerializer(serializers.ModelSerializer):
    tabs = TabSerializer(many=True)

    class Meta:
        model = Squeeze
        fields = ['id', 'title', 'tabs', 'image']
    
    def create(self, validated_data):
        tabs_data = validated_data.pop('tabs')
        user = self.context['user']
        squeeze = Squeeze.objects.create(**validated_data)
        for tab_data in tabs_data:
            tab, created = Tab.objects.get_or_create(**tab_data, user=user)
            squeeze.tabs.add(tab)
        return squeeze