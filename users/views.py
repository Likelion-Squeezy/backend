from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.exceptions import NotAuthenticated
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from squeeze.models import Squeeze
from eezy.models import Eezy
from .models import User
from .serializers import UserProfileSerializer, RegisterSerializer



class UserView(APIView):
    permission_classes = [IsAuthenticated]
    

    @method_decorator(cache_page(60*5))  # 5분 동안 결과 캐싱
    def get(self, request):
        user = request.user

        if user.is_anonymous:
            raise NotAuthenticated("자격 인증이 필요합니다.")

        # 사용자 정보와 함께 응답 생성 (시리얼라이저 사용)
        user_serializer = UserProfileSerializer(user)
        return Response(user_serializer.data, status=status.HTTP_200_OK)
    
class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = User.objects.create(
                username=serializer.validated_data['username'],
                email=serializer.validated_data['email'],
                password=serializer.validated_data['password'],
            )
            return Response({"message": "계정 생성이 완료되었습니다.", "id": user.id}, status=status.HTTP_201_CREATED)