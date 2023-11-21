
from django.urls import path
from .views import *


urlpatterns = [
    path('',home,name='home'),
    
    path('pizza-bases/', PizzaBaseListCreateView.as_view(), name='pizza-base-list'),
    path('pizza-bases/create/', PizzaBaseListCreateView.as_view(), name='pizza-base-create'),
    
    path('cheese-types/', CheeseListCreateView.as_view(), name='cheese-list'),
    path('cheese-types/create/', CheeseListCreateView.as_view(), name='cheese-create'),
    
    
    path('toppings/', ToppingsListCreateView.as_view(), name='toppings-list'),
    path('toppings/create/', ToppingsListCreateView.as_view(), name='toppings-create'),
    
    path('create-order/', CreateOrderView.as_view() , name='create_order'),
    path('list-order/', OrderListView.as_view() , name='list_order'),

    path('order-status/<int:id>', OrderStatusDetailView.as_view() , name='order_status'),


]
