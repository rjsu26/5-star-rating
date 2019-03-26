from django.shortcuts import render,HttpResponse
# from rest_framework import viewsets
from rest_framework import generics
from reviews import models
from . import serializers
# Create your views here.

class ProductList(generics.ListCreateAPIView):
    queryset= models.product.objects.all()
    serializer_class=serializers.ProductSerializer

class ReviewList(generics.ListCreateAPIView):
    serializer_class= serializers.RatingSerializer
    def get_queryset(self):
        token = self.kwargs['number']
        query_set= models.feedback.objects.filter(item=token)
        return query_set

