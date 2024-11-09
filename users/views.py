from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.exceptions import NotAuthenticated
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from squeeze.models import Squeeze
from eezy.models import Eezy
from squeeze.serializers import SqueezeSerializer
from django.db import models
from django.contrib.auth.models import AbstractUser

class UserView(APIView):
    permission_classes = [IsAuthenticated]
    

    @method_decorator(cache_page(60*5))  # 5분 동안 결과 캐싱
    def get(self, request):
        user = request.user

        if user.is_anonymous:
            raise NotAuthenticated("자격 인증이 필요합니다.")

        # Squeeze 정보 가져오기
        squeeze_qs = Squeeze.objects.filter(user=user).prefetch_related('tabs')
        squeeze_data = [
            {
                "id": squeeze.id,
                "title": squeeze.title,
                "count": squeeze.tabs.count(),
            }
            for squeeze in squeeze_qs
        ]

        # Eezy 정보 가져오기
        eezy_qs = Eezy.objects.filter(user=user).select_related('tab')
        eezy_data = [
            {
                "id": eezy.id,
                "title": eezy.title,
            }
            for eezy in eezy_qs
        ]

        # 사용자 정보와 함께 응답 생성
        response_data = {
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "squeeze": squeeze_data,
            "eezy": eezy_data,
        }

        return Response(response_data, status=status.HTTP_200_OK)
