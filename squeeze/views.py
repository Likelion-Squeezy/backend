from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from .models import Squeeze

from tabs.serializers import TabSerializer
from .serializers import SqueezeSerializer


# Create your views here.

class SqueezeView(APIView):
    def get(self, request, squeeze_id):
        try:
            squeeze = Squeeze.objects.get(id=squeeze_id)
            serializer = SqueezeSerializer(squeeze)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Squeeze.DoesNotExist:
            return Response({"error": "Eezy not found"}, status=status.HTTP_404_NOT_FOUND)