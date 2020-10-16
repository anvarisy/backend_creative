from django.shortcuts import render
from rest_framework import generics
from api.serializer import CategorySerializer
from api.models import category
# Create your views here.
        # Untuk hasil url?style=param
        # style = self.request.query_params.get('style', None)
        # Untuk hasil url/param
        # style = self.kwargs['style']
class ApiStyle(generics.ListAPIView):
    serializer_class = CategorySerializer
    def get_queryset(self):
        queryset = category.objects.all()
        return queryset