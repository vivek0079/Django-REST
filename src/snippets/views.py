from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import Snippet
from .serializers import SnippetSerializer

@csrf_exempt
def snippet_list_or_create(request):
    if request.method == 'GET':
        snippet = Snippet.objects.all()
        serializer = SnippetSerializer(snippet, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.data, status=400)

@csrf_exempt
def snippet_detail(request, pk=None):
    try:
        snippet = Snippet.objects.get(pk=pk)
    except:
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return JsonResponse(serializer.data, status=200)
    
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.data, status=400)
    
    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)

