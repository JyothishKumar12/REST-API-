from django.shortcuts import render
from .models import Task
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.


@api_view(['GET'])
def apioverview(request):
    api_urls = {'name':hai}
    return Response(api_urls)
