from django.contrib import admin
from .models import PizzaBase, CheeseType, Toppings, PizzaOrder, OrderStatus, PizzaDetails

# Register your models here.


admin.site.register(PizzaBase)
admin.site.register(CheeseType)
admin.site.register(Toppings)
admin.site.register(PizzaOrder)
admin.site.register(OrderStatus)
admin.site.register(PizzaDetails)
