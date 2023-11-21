# zenduty-pizza-app

<br />Installation
<br />1. Clone the repository:

```bash
   https://github.com/hacky-tosh/zenduty-pizza-app.git
```
2. Install the required dependencies:
<br />

    ```bash
    
      cd zenduty-pizza-app
      pip install -r requirements.txt
     
    ```
<br />3. Apply the database migrations:
     ```bash 
     
         python manage.py makemigrations
         python manage.py migrate
     
     ```

<br />4. Run the development server:
```bash
      python manage.py runserver
```
In another terminal
```bash
   python -m celery -A pizzeria worker
```

<br />The application will be accessible at http://localhost:8000/.


<br />##API Endpoints

<br />#Create Pizza Bases

<br />Endpoint: /api/pizza-bases/create/
<br />Method: POST
<br />Request Body:
```bash
  [
    {
        "name": "Thin Crust",
        "price": 7.99
    },
    {
        "name": "Thick Crust",
        "price": 9.99
    },
    {
        "name": "Gluten-Free",
        "price": 10.99
    }
]

```
<br /># Get All Pizza Base

<br />Endpoint: /api/pizza-bases/
<br />Method: GET

_________________________________________________
<br />#Create Cheese

<br />Endpoint: /api/cheese-types/create/
<br />Method: POST
<br />Request Body:
```bash
  [
    {
        "name": "Mozzarella",
        "price": 1.5
    },
    {
        "name": "Cheddar",
        "price": 2.0
    },
    {
        "name": "Parmesan",
        "price": 2.5
    }
]

```
<br /># Get All Cheese

<br />Endpoint: /api/cheese-types/
<br />Method: GET

_________________________________________________
<br />#Create Toppings

<br />Endpoint: /api/toppings/create/
<br />Method: POST
<br />Request Body:
```bash
  [
    {
        "name": "Mushrooms",
        "price": 1.0
    },
    {
        "name": "Pepperoni",
        "price": 1.5
    },
    {
        "name": "Onions",
        "price": 0.75
    },
    {
        "name": "Bell Peppers",
        "price": 1.25
    },
    {
        "name": "Olives",
        "price": 1.0
    }
]
```
<br /># Get All Toppings

<br />Endpoint: /api/toppings/
<br />Method: GET


_________________________________________________


<br />#Create Pizza Order

<br />Endpoint: /api/create-order/
<br />Method: POST
<br />Request Body:
```bash
 {
    "customer_name": "Ashutosh",
    "customer_contact": "9569461019",
    "delivery_address": "India",
    "pizzas": [
         {
            "base_id": 2,
            "cheese_id": 3,
            "topping_ids": [1,2,3,4,5]
        },
        {
            "base_id": 1,
            "cheese_id": 2,
            "topping_ids": [1,2,3,4,5]
        }
    ]
}

```
<br />Response Body:

```bash
{
    "order_id": 1,
    "pizzas": [
        ..........
            ]
        }
    ]
}
```



<br /># Get Order Status By order Id

<br />Endpoint: /api/order-status/<int:orderId>
            Ex: /api/order-status/1
                
<br />Method: GET

<br />Response Body:

```bash

{
    "id": 1,
    "order_id": 1,
    "status": "Placed",
    "timestamp": "2023-11-21T13:10:41.513421Z"
}

```

<br /> After 1 Min

<br />Response Body:

```bash

{
    "id": 1,
    "order_id": 1,
    "status": "Accepted",
    "timestamp": "2023-11-21T13:10:41.513421Z"
}

```

<br /> After 2 Min

<br />Response Body:

```bash

{
    "id": 1,
    "order_id": 1,
    "status": "Preparing",
    "timestamp": "2023-11-21T13:10:41.513421Z"
}

```
<br /> After 3 Min

<br />Response Body:

```bash

{
    "id": 1,
    "order_id": 1,
    "status": "Dispatched",
    "timestamp": "2023-11-21T13:10:41.513421Z"
}

```

<br /> After 3 Min

<br />Response Body:

```bash

{
    "id": 1,
    "order_id": 1,
    "status": "Delivered",
    "timestamp": "2023-11-21T13:10:41.513421Z"
}

```















