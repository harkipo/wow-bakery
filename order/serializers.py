from .models import *
from rest_framework import serializers

class OfferSerializer(serializers.ModelSerializer):
    """
    Serializer class for Offer Model
    """
    class Meta:
        model = Offer 
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    """
    Serializer class for Order Model
    """
    class Meta:
        model = Order 
        fields = '__all__'
        depth = 1

class OrderItemsSerializer(serializers.ModelSerializer):
    """
    Serializer class for OrderItems Model
    """
    class Meta:
        model = OrderItems 
        fields = '__all__'
        depth = 1