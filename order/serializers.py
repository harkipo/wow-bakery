from .models import *
from django.contrib.auth.models import User
from rest_framework import serializers

class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer 
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order 
        fields = '__all__'
        depth = 1

class OrderItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItems 
        fields = '__all__'
        depth = 1