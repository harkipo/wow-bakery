from django.db import models


class Ingredients(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'ingredients'


class BakeryItem(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    cost_price = models.IntegerField(blank=True,null=True)
    sell_price = models.IntegerField(blank=True,null=True)
    quantity_sold = models.IntegerField(default=0)


    class Meta:
        db_table = 'api_logs'


class BakeryItemIngredients(models.Model):
    item = models.ForeignKey(BakeryItem,on_delete=models.CASCADE,primary_key=False)
    ingredient = models.ForeignKey(Ingredients,on_delete=models.CASCADE,primary_key=False)
    percentage_used = models.IntegerField(blank=True,null=True)

    class Meta:
        db_table = 'bakery_item_ingredients'
        
