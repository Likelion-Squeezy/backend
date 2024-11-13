from rest_framework import serializers
from .models import User
from squeeze.models import Squeeze
from eezy.models import Eezy

class UserProfileSerializer(serializers.ModelSerializer):
    history = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'history']

    def get_history(self, obj):
        squeeze_qs = Squeeze.objects.filter(user=obj).order_by('-created_at')
        eezy_qs = Eezy.objects.filter(user=obj).order_by('-created_at')

        history = [
            {
                "type": "squeezy",
                "id": squeeze.id,
                "title": squeeze.title,
                "created_at": squeeze.created_at,
            }
            for squeeze in squeeze_qs
        ] + [
            {
                "type": "eezy",
                "id": eezy.id,
                "title": eezy.title,
                "created_at": eezy.created_at,
            }
            for eezy in eezy_qs
        ]

        return sorted(history, key=lambda x: x['created_at'], reverse=True)