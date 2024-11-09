from rest_framework import serializers
from django.contrib.auth import get_user_model
from squeeze.serializers import SqueezeSerializer
from eezy.serializers import EezySerializer

User = get_user_model()

class UserProfileSerializer(serializers.ModelSerializer):
    squeeze = SqueezeSerializer(many=True)
    eezy = EezySerializer(many=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'squeeze', 'eezy']
