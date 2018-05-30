from django.http import Http404

from rest_framework import generics, mixins

from .models import Snippet
from .serializers import SnippetSerializer

class SnippetListCreateView(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


class SnippetRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


# class SnippetListCreateView(APIView):
#     def get(self, request, format=None):
#         snippet = Snippet.objects.all()
#         serializer = SnippetSerializer(snippet, many=True)
#         return Response(serializer.data)
    
#     def post(self, request, format=None):
#         serializer = SnippetSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(url=request.build_absolute_uri())
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

# class SnippetRetrieveUpdateView(APIView):
#     def get_object(self, pk):
#         try:
#             return Snippet.objects.get(pk=pk)
#         except:
#             raise Http404
    
#     def get(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = SnippetSerializer(snippet)
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = SnippetSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save(url=request.build_absolute_uri())
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         print(snippet)
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
# class SnippetDeleteView(APIView):
#     def get_object(self, pk):
#         try:
#             snippet = Snippet.obects.get(pk=pk)
#         except:
#             raise Http404
    
#     def delete(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
