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
                "count": squeeze.tabs.count(),
                "created_at": squeeze.created_at,
            }
            for squeeze in squeeze_qs
        ] + [
            {
                "type": "eezy",
                "id": eezy.id,
                "title": eezy.title,
                "content": eezy.content,
                "created_at": eezy.created_at,
            }
            for eezy in eezy_qs
        ]

        return sorted(history, key=lambda x: x['created_at'], reverse=True)
    

class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()
    password_check = serializers.CharField()
    
    def validate(self, data):
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        password_check = data.get('password_check')

        if not all([username, email, password, password_check]):
            raise serializers.ValidationError("모든 필드를 입력해주세요.")
        
        if password != password_check:
            raise serializers.ValidationError("비밀번호가 일치하지 않습니다.")
        
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError("이미 가입한 이메일입니다.")   
        
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError("이미 사용중인 아이디입니다.")
        
        return data
    
class LoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()
    
    def validate(self, data):
        email = data.get('email')
        password = data.get('password')
        
        if not all([email, password]):
            raise serializers.ValidationError("모든 필드를 입력해주세요.")
        
        if not User.objects.filter(email=email).exists():
            raise serializers.ValidationError("가입하지 않은 이메일입니다.")
        
        return data