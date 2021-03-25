from .models import *
from django.contrib.auth.models import User
from rest_framework import serializers

class IngredientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredients 
        fields = '__all__'

class BakeryItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = BakeryItem 
        fields = '__all__'

class BakeryItemIngredientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BakeryItemIngredients 
        fields = '__all__'
        depth = 1