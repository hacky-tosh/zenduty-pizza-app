from rest_framework import serializers
from .models import *

class PizzaBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = PizzaBase
        fields = '__all__'
        
class CheeseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheeseType
        fields = '__all__'
        
class ToppingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Toppings
        fields = '__all__'
        
class PizzaDetailsSerializer(serializers.ModelSerializer):
    base = PizzaBaseSerializer()
    cheese = CheeseSerializer()
    toppings = ToppingsSerializer(many=True)

    class Meta:
        model = PizzaDetails
        fields = ('id', 'price', 'base', 'cheese', 'toppings')

class OrderStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderStatus
        fields = ('id','order_id','status', 'timestamp') 
        
        
class PizzaOrderSerializer(serializers.ModelSerializer):
    pizzas = PizzaDetailsSerializer(many=True)
    order_status = OrderStatusSerializer(source='orderstatus_set', many=True) 

    class Meta:
        model = PizzaOrder
        fields = ('id', 'customer_name', 'customer_contact', 'delivery_address',
                  'total_price', 'order_time', 'pizzas', 'order_status')
        