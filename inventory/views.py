from rest_framework import status , mixins
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from .models import *
from rest_framework.viewsets import ModelViewSet , ReadOnlyModelViewSet , GenericViewSet
from rest_framework.permissions import IsAuthenticated , IsAdminUser
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView

class IngredientViewSet(ModelViewSet):
    queryset = Ingredients.objects.all()
    serializer_class = IngredientsSerializer
    permission_classes = [IsAuthenticated&IsAdminUser]

class BakeryItemListViewSet(ReadOnlyModelViewSet):
    

    queryset = BakeryItem.objects.all()
    serializer_class = BakeryItemSerializer

class BakeryItemDetailViewSet(mixins.CreateModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    GenericViewSet):

    queryset = BakeryItem.objects.all()
    serializer_class = BakeryItemSerializer
    permission_classes = [IsAuthenticated&IsAdminUser]


class BakeryItemIngredientView(APIView):
    permission_classes = [IsAuthenticated&IsAdminUser]

    def post(self, request, format=None):
        data = request.data
        item_id = data.get("item_id",None)
        ingredient_id = data.get("ingredient_id",None)
        percentage_used = data.get("percentage_used",None)
        if item_id and ingredient_id:
            try:
                BakeryItemIngredients.objects.update_or_create(item_id=item_id,ingredient_id=ingredient_id,percentage_used=percentage_used)
                message = "Ingredient added to item successfully"
                status = 200
            except Exception as e:
                message = str(e)
                status = 400
        else:
            message = "Please provide item id and ingredient id"
            status = 400
        return Response({"details":message},status=status)


    def delete(self, request, format=None):
        data = request.data
        item_id = data.get("item_id",None)
        ingredient_id = data.get("ingredient_id",None)
        if item_id and ingredient_id:
            try:
                data = BakeryItemIngredients.objects.filter(item_id=item_id,ingredient_id=ingredient_id)
                if data:
                    data.delete
                    message = "Ingredient deleted from item successfully"
                    status = 200
                else:
                    message = "Ingredient not found"
                    status = 400

            except Exception as e:
                message = str(e)
                status = 400
        else:
            message = "Please provide item id and ingredient id"
            status = 400
        return Response({"details":message},status=status)
        


