from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


from .models import Squeeze

from tabs.serializers import TabSerializer
from .serializers import SqueezeSerializer

from dotenv import load_dotenv
import os
import openai
import json

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
client = openai.OpenAI(api_key=openai.api_key)


# Create your views here.

class SqueezeView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, squeeze_id):
        try:
            squeeze = Squeeze.objects.get(id=squeeze_id)
            serializer = SqueezeSerializer(squeeze)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Squeeze.DoesNotExist:
            return Response({"error": "Eezy not found"}, status=status.HTTP_404_NOT_FOUND)
    
    def post(self, request):
        user = request.user
        tabs = request.data.get('tabs')
        image = request.data.get('image')
        if not tabs:
            return Response({"error": "Tabs are required"}, status=status.HTTP_400_BAD_REQUEST)

        # Create a prompt for grouping similar tabs
        prompt = (
            "다음 탭들을 비슷한 주제끼리 묶어서 북마크를 생성해 주세요. "
            "각 그룹은 주제와 함께 제공되어야 합니다. "
            "탭 정보는 다음과 같습니다:\n\n"
        )
        for tab in tabs:
            prompt += f"제목: {tab['title']}, URL: {tab['url']}, favicon: {tab['favicon']}\n"
        prompt += (
            "\n출력 형식은 다음과 같은 JSON이어야 합니다:\n"
            "{\n"
            "  \"response\": [\n"
            "    {\n"
            "      \"title\": \"북마크 제목1\",\n"
            "      \"tabs\": [\n"
            "        {\"title\": \"test1\", \"url\": \"test1.com\", \"favicon\": \"favicon1\"},\n"
            "        {\"title\": \"test2\", \"url\": \"test2.com\", \"favicon\": \"favicon2\"}\n"
            "      ]\n"
            "    },\n"
            "    {\n"
            "      \"title\": \"북마크 제목2\",\n"
            "      \"tabs\": [\n"
            "        {\"title\": \"test3\", \"url\": \"test3.com\", \"favicon\": \"favicon3\"},\n"
            "        {\"title\": \"test4\", \"url\": \"test4.com\", \"favicon\": \"favicon4\"}\n"
            "      ]\n"
            "    }\n"
            "  ]\n"
            "}\n"
        )

        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "너는 탭들을 비슷한 주제끼리 묶어서 북마크를 생성해주는 역할이야."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=1000
            )
            result = response.choices[0].message.content.strip()
            result = json.loads(result)
            print(result)
            
            for group in result['response']:
                squeeze_serializer = SqueezeSerializer(data=group, context={"user": user})
                if squeeze_serializer.is_valid():   
                    squeeze = squeeze_serializer.save(user=user)
                else:
                    return Response({"message": "squeeze 생성에 문제가 생겼습니다.", "detail": squeeze_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

            # Process the result to create bookmarks without favicon
        except Exception as e:
            return Response({"message": "OpenAI API 요청 과정에서 문제가 발생했습니다.", "detail":str(e)}, status=status.HTTP_400_BAD_REQUEST)

        serializer = SqueezeSerializer(data=request.data)

        return Response({"message": "test"}, status=status.HTTP_200_OK)