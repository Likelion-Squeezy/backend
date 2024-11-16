from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import openai
import json

from tabs.models import Tab
from users.models import User
from eezy.models import Eezy

from tabs.serializers import TabSerializer
from .serializers import EezySerializer
from dotenv import load_dotenv
import os

from rest_framework.permissions import IsAuthenticated

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
client = openai.OpenAI(api_key=openai.api_key)

class EezyView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, eezy_id):
        if not eezy_id:
            return Response({"message": "Eezy id를 입력해주세요."}, status=status.HTTP_400_BAD_REQUEST)
        try:
            eezy = Eezy.objects.get(id=eezy_id)
            serializer = EezySerializer(eezy)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Eezy.DoesNotExist:
            return Response({"message": "해당 eezy가 존재하지 않습니다."}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        user = request.user

        if user.eezy_count > 0:
            user.eezy_count -= 1
            user.save()
        else:
            return Response({"message": "eezy를 모두 사용했습니다."}, status=status.HTTP_400_BAD_REQUEST)

        tab_serializer = TabSerializer(data=request.data)
        html_content = request.data.get('script')
        if not html_content:
            return Response({"message": "html 코드가 없습니다."}, status=status.HTTP_400_BAD_REQUEST)
        
        # tab 인스턴스 생성
        if tab_serializer.is_valid():
            tab = tab_serializer.save(user=user)
        else:
            return Response(tab_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


        # 입력(prompt)의 문자열 길이 제한
        max_input_length = 3500
        if len(html_content) > max_input_length:
            return Response({"message": f"입력 제한 초과: {max_input_length} 글자"}, status=status.HTTP_400_BAD_REQUEST)   

        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "너는 웹 페이지의 내용을 노션 페이지에 정리하기 좋은 markdown으로 요약해주는 역할이야."},
                    {"role": "user", "content": (
                        "다음 HTML 콘텐츠를 요약해 주세요. "
                        "요약본은 노션에 적합한 마크다운 형식으로 작성해 주세요. "
                        "결과는 마크다운 형식의 문자열로 반환해 주세요:\n\n"
                        f"{html_content}\n\n"
                    )}
                ],
                max_tokens=900
            )
            result = response.choices[0].message.content.strip()

            # Directly use the string response
            eezy = Eezy.objects.create(title=tab.title, content=result, tab=tab, user=user)
            serializer = EezySerializer(eezy)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message": "openai api 요청 과정에서 문제가 발생했습니다."}, status=status.HTTP_400_BAD_REQUEST)
    