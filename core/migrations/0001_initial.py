# Generated by Django 4.2.7 on 2023-11-18 09:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CheeseType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PizzaBase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PizzaDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pizza_number', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('base', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.pizzabase')),
                ('cheese', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.cheesetype')),
            ],
        ),
        migrations.CreateModel(
            name='Toppings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PizzaOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=100)),
                ('customer_contact', models.CharField(max_length=20)),
                ('delivery_address', models.TextField()),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('order_time', models.DateTimeField(auto_now_add=True)),
                ('pizza_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.pizzadetails')),
            ],
        ),
        migrations.AddField(
            model_name='pizzadetails',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.pizzaorder'),
        ),
        migrations.CreateModel(
            name='OrderStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=100)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.pizzaorder')),
            ],
        ),
    ]
