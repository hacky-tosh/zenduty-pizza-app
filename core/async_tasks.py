from celery import shared_task
from datetime import timedelta
from .models import OrderStatus
from django.utils import timezone  


@shared_task
def update_order_status(order_id):
    try:
        order = OrderStatus.objects.get(pk=order_id)
    except OrderStatus.DoesNotExist:
        print(f"Order with ID {order_id} does not exist")
        return

    elapsed_time = (timezone.now() - order.timestamp).total_seconds() / 60  # Elapsed time in minutes
    print(elapsed_time)
    print(order.status)
    print("===========")
    # Update status based on time elapsed
    if elapsed_time <= 1:
        if order.status != 'Accepted':
            order.status = 'Accepted'
            order.save()
    elif 1 < elapsed_time <= 2:
        if order.status != 'Preparing':
            order.status = 'Preparing'
            order.save()
    elif 2 < elapsed_time <= 5:
        if order.status != 'Dispatched':
            order.status = 'Dispatched'
            order.save()
    else:
        if order.status != 'Delivered':
            order.status = 'Delivered'
            order.save()
    if order.status != 'Delivered':        
            update_order_status.apply_async(args=[order.id],countdown=60)
