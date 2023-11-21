from django.shortcuts import render,HttpResponse
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import *
from .serializer import *
from django.http import JsonResponse
from django.db import transaction
from django.utils import timezone
from datetime import timedelta
from .async_tasks import update_order_status





# Create your views here.


def home(request):
    return HttpResponse("Hello World")


class PizzaBaseListCreateView(generics.ListCreateAPIView):
    queryset = PizzaBase.objects.all()
    serializer_class = PizzaBaseSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=True)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  

class CheeseListCreateView(generics.ListCreateAPIView):
    queryset = CheeseType.objects.all()
    serializer_class = CheeseSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data,many=True)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class ToppingsListCreateView(generics.ListCreateAPIView):
    queryset = Toppings.objects.all()
    serializer_class = ToppingsSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data,many=True)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
class PizzaDetailsListCreateView(generics.ListCreateAPIView):
    queryset = PizzaDetails.objects.all()
    serializer_class = PizzaOrderSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data,many=True)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



class OrderStatusDetailView(generics.RetrieveAPIView):
    queryset = OrderStatus.objects.all()
    serializer_class = OrderStatusSerializer
    lookup_field = 'id'

    def get_object(self):
        order_status_id = self.kwargs['id']  
        return self.queryset.get(id=order_status_id)


class OrderListView(generics.ListAPIView):
    queryset = OrderStatus.objects.all()
    serializer_class = OrderStatusSerializer




class CreateOrderView(APIView):
    @transaction.atomic
    def post(self, request, *args, **kwargs):
        if request.content_type == 'application/json':
            data = request.data

            pizzas_data = data.get('pizzas', [])
            customer_name = data.get('customer_name')
            customer_contact = data.get('customer_contact')
            delivery_address = data.get('delivery_address')

            if not all(isinstance(pizza, dict) for pizza in pizzas_data):
                return JsonResponse({'error': 'Invalid pizza data format'}, status=status.HTTP_400_BAD_REQUEST)

            order = PizzaOrder.objects.create(
                customer_name=customer_name,
                customer_contact=customer_contact,
                delivery_address=delivery_address,
                total_price=0  # Initialized total price to 0
            )

            created_pizzas = []

            for pizza_data in pizzas_data:
                base_id = pizza_data.get('base_id')
                cheese_id = pizza_data.get('cheese_id')
                topping_ids = pizza_data.get('topping_ids', [])

                base = PizzaBase.objects.get(pk=base_id)
                cheese = CheeseType.objects.get(pk=cheese_id)
                toppings = Toppings.objects.filter(pk__in=topping_ids)

                if base and cheese and toppings.count() == 5:
                    base_price = base.price
                    cheese_price = cheese.price
                    toppings_price = sum(t.price for t in toppings)

                    total_price = base_price + cheese_price + toppings_price

                    pizza_details = PizzaDetails.objects.create(
                        base=base,
                        cheese=cheese,
                        price=total_price,
                        order=order  
                    )
                    pizza_details.toppings.add(*toppings)

                    created_pizzas.append({
                        'id': pizza_details.id,
                        'price': total_price,
                        'base': {'id': base_id, 'name': base.name, 'price': str(base.price)},
                        'cheese': {'id': cheese_id, 'name': cheese.name, 'price': str(cheese.price)},
                        'toppings': [{'id': t.id, 'name': t.name, 'price': str(t.price)} for t in toppings]
                    })

            # Calculate total price for the order and update the order's total price
            order.total_price = sum(pizza['price'] for pizza in created_pizzas)
            order.save()
            
            
            

            # Adding OrderStatus entry for the newly placed order
            OrderStatus.objects.create(order_id=order, status="Placed")

            update_order_status.apply_async(args=[order.id],countdown=60)
            return JsonResponse({'order_id': order.id, 'pizzas': created_pizzas})

        return JsonResponse({'error': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)


