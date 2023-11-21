from django.db import models

# Create your models here.

class PizzaBase(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2,default=0.00)
    
    def __str__(self):
        return self.name

class CheeseType(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2,default=0.00)
    
    def __str__(self):
        return self.name


class Toppings(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2,default=0.00)
    
    def __str__(self):
        return self.name

class PizzaOrder(models.Model):
    customer_name = models.CharField(max_length=100)
    customer_contact = models.CharField(max_length=20)
    delivery_address = models.TextField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    order_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.customer_name + " " + self.customer_contact

class OrderStatus(models.Model):
    order_id = models.ForeignKey(PizzaOrder, on_delete=models.CASCADE)
    status = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.status

class PizzaDetails(models.Model):
    base = models.ForeignKey(PizzaBase, on_delete=models.CASCADE)
    cheese = models.ForeignKey(CheeseType, on_delete=models.CASCADE)
    toppings = models.ManyToManyField(Toppings)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    order = models.ForeignKey(PizzaOrder, related_name='pizzas', on_delete=models.CASCADE, null=True)  # Allow null for existing rows

    def __str__(self):
        return self.base.name + " " + self.cheese.name
