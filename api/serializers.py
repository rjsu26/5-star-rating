from rest_framework import serializers
from reviews import models

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.feedback
        fields=(
            'id',
            'user',
            'rating',
        )

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.product
        fields=(
            'id',
            'title',
            'description',
            'review',
        )