from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL) # User 모델이 저장된 후에 실행
def create_auth_token(sender, instance=None, created=False, **kwargs): # user instance를 전달받음
    if created:  # 새로 생성된 사용자일 때만 토큰 생성
        Token.objects.create(user=instance)