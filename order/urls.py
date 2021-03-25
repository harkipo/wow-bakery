from django.urls import path
from order.views import OrderView


urlpatterns = [
    path('', OrderView.as_view(), name='order_create'),
    path('<int:pk>/', OrderView.as_view(), name='order_view'),
    
]

