from django.db import models
from django.contrib.auth.models import User
from inventory.models import BakeryItem

class Offer(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    discount_percentage = models.IntegerField(blank=True,null=True)

    class Meta:
        db_table = 'offer'


class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,primary_key=False)
    total_value = models.IntegerField(blank=True,null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    offer = models.ForeignKey(Offer,on_delete=models.CASCADE,primary_key=False,blank=True, null=True)


    class Meta:
        db_table = 'order'


class OrderItems(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE,primary_key=False)
    item = models.ForeignKey(BakeryItem,on_delete=models.CASCADE,primary_key=False)
    quantity = models.IntegerField(blank=True,null=True)

    class Meta:
        db_table = 'order_items'
        
