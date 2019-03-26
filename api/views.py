from django.shortcuts import render
# from rest_framework import viewsets
from rest_framework import generics
from reviews import models
from . import serializers
# Create your views here.

class ProductList(generics.ListCreateAPIView):
    queryset= models.product.objects.all()
    serializer_class=serializers.ProductSerializer

class ReviewList(generics.ListCreateAPIView):
    queryset=models.feedback.objects.all()
    serializer_class= serializers.RatingSerializer

# class feedbackViewSet(viewsets.ModelViewSet):
#     queryset= models.feedback.objects.all()
#     serializer_class=serializers.RatingSerializer

# class productViewSet(viewsets.ModelViewSet):
#     queryset= models.product.objects.all()
#     serializer_class=serializers.ProductSerializer

