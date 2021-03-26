from rest_framework import status
from rest_framework.response import Response
from .serializers import *
from .models import *
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.views import APIView
import json


class OfferViewSet(ModelViewSet):
    """
    API view for offers 
    Methods - POST , PATCH , DELETE
    Function - Create , Update and Delete offers
    """
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
    permission_classes = [IsAuthenticated & IsAdminUser]


class OrderView(APIView):
    """
    API view for offers 
    Methods - GET , POST
    """
    permission_classes = [IsAuthenticated & IsAdminUser]

    def get(self, request, pk, format=None):
        """
        Retrieve specific order
        """
        pk = self.kwargs['pk']
        order = Order.objects.filter(id=pk)
        if order:
            order = order[0]
            order_serializer = OrderSerializer(
                order, context={'request': request})
            return Response(order_serializer.data)
        else:
            return Response({"details": "Order not found"}, status=400)

    def post(self, request, format=None):
        """
        Create order from cart items and return details for billing
        """
        try:
            data = request.data
            address = data.get("address", None)
            state = data.get("state", None)
            city = data.get("city", None)
            offer_id = data.get("offer_id", None)
            items = data.get("item", None)
            items = json.loads(items)
            user = request.user
            total_value = 0
            final_items = []
            order = Order.objects.create(
                user=user, address=address, state=state, city=city, offer_id=offer_id)
            discount_percentage = order.offer.discount_percentage
            print("discount percentage >>>", discount_percentage)
            for item in items:
                print(item)
                item_id = item.get("item_id")
                quantity = item.get("quantity")
                order_item = OrderItems.objects.create(
                    order=order, item_id=item_id, quantity=quantity)
                bakery_item = order_item.item
                bakery_item.quantity_sold = bakery_item.quantity_sold + quantity
                bakery_item.save()
                total_value = total_value + \
                    (int(order_item.item.sell_price) * int(quantity))
                order_item_serializer = OrderItemsSerializer(
                    order_item, context={'request': request})
                final_items.append(order_item_serializer.data)
            print("total value >>", total_value)
            total_value = ((100-discount_percentage)/100)*total_value
            order.total_value = total_value
            order.save()
            order_serializer = OrderSerializer(
                order, context={'request': request})
            print("total value after discount >>", total_value)

            return Response({"order_details": order_serializer.data, "item_list": final_items})
        except Exception as e:
            return Response({"details": str(e)}, status=400)
