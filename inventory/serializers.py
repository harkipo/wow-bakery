from .models import *
from rest_framework import serializers


class IngredientsSerializer(serializers.ModelSerializer):
    """
    Serializer class for Ingredients Model
    """
    class Meta:
        model = Ingredients
        fields = '__all__'


class BakeryItemSerializer(serializers.ModelSerializer):
    """
    Serializer class for BakeryItem Model
    """
    class Meta:
        model = BakeryItem
        fields = '__all__'


class BakeryItemIngredientsSerializer(serializers.ModelSerializer):
    """
    Serializer class for BakeryItemIngredients Model
    """
    class Meta:
        model = BakeryItemIngredients
        fields = '__all__'
        depth = 1
