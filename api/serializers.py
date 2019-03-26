from rest_framework import serializers
from reviews import models

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.product
        fields=(
            'id',
            'title',
            'description',
            'review',
        )
class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.feedback
        fields=(
            'user',
            'rating',
            'item',
        )
    