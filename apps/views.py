from django.shortcuts import render
from .models import Task
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serailizer import TaskSerializer
# Create your views here.


@api_view(['GET'])
def apioverview(request):
    api_urls = {'name':'hai'}
    return Response(api_urls)

@api_view(['GET'])
def tasklist(request):
    task = Task.objects.all()
    serailizer = TaskSerializer(task, many=True)
    return Response(serailizer.data)

@api_view(['POST'])
def taskPost(request):
    serializer = TaskSerializer(data= request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)


@api_view(['GET'])
def taskDetail(request,pk):
    task = Task.objects.get(id=pk)
    serailizer = TaskSerializer(task, many=False)
    return Response(serailizer.data)



@api_view(['POST'])
def taskUpdate(request,pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=task, data= request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)



@api_view(['DELETE'])
def taskDelete(request,pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return Response(serializer.data)


