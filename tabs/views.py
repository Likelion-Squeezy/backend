from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Tab
from .serializers import TabSerializer

# Create your views here.
class TabView(APIView):
    def get(self, request):
        title = request.query_params.get('title')
        if title:
            tabs = Tab.objects.filter(title__icontains=title)
            serializer = TabSerializer(tabs, many=True)
            return Response(serializer.data)
        return Response({'error': 'Title parameter is required'}, status=400)