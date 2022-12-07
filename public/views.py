from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.

class IndexView(APIView):
    
    def get(self, request, format=None):
        content = {
            'Message':'Welcome to LeaveSoft '
        }
        return Response(content)