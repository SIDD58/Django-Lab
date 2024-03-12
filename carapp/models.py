from django.contrib.auth.models import User
from django.db import models


# CarType Model

class CarType(models.Model):
    name = models.CharField(max_length=150)

    # __str__ method
    def __str__(self):
        return self.name


# Vehicle

class Vehicle(models.Model):
    car_type = models.ForeignKey(CarType, related_name='vehicles', on_delete=models.CASCADE)
    car_name = models.CharField(max_length=200)
    car_price = models.DecimalField(max_digits=10, decimal_places=6)

    CAR_FEATURE_CHOICES = [
        ('Cruise','Cruise'),
        ('Control','Control'),
        ('Audio','Audio'),
        ('Interface','Interface'),
        ('Airbags','Airbags'),
        ('Air', 'Air'),
        ('Conditioning', 'Conditioning'),
        ('Seat' , 'Seat'),
        ('Heating' , 'Heating'),
        ('ParkAssist' , 'ParkAssist'),
        ('Power' , 'Power'),
        ('Steering' , 'Steering'),
        ('Reversing' , 'Reversing'),
        ('Camera', 'Camera'),
        ('Auto' , 'Auto'),
        ('Start / Stop' , 'Start / Stop')
    ]

    car_features = models.CharField(max_length=100,choices=CAR_FEATURE_CHOICES,default='Seat')
    inventory = models.PositiveIntegerField(default=10)
    instock = models.BooleanField(default=True)
    # optional Field
    description = models.TextField(blank=True)

    # __str__ method
    def __str__(self):
        return self.car_name


# Buyers

class Buyer(User):
    AREA_CHOICES = [
        ('W', 'Windsor'),
        ('LS', 'LaSalle'),
        ('A', 'Amherstburg'),
        ('L', 'Lakeshore'),
        ('LE', 'Leamington'),
        ('C', 'Chatham'),
        ('T','Toronto'),
        ('Wa','Waterloo'),
    ]
    shipping_address = models.CharField(max_length=300, null=True, blank=True)
    # default value changed to Chatham
    area = models.CharField(max_length=2, choices=AREA_CHOICES, default='C')
    interested_in = models.ManyToManyField(CarType)
    # phone number added
    phone_number = models.CharField(max_length=10, null=True, blank=True)

    # __str__ method
    def __str__(self):
        return self.username


# OrderVehicle

class OrderVehicle(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    STATUS_CHOICES = [
        ('0', 'cancelled'),
        ('1', 'placed'),
        ('2', 'shipped'),
        ('3', 'delivered'),
    ]
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='1')
    date = models.DateTimeField(auto_now=True)

    # __str__ method
    def __str__(self):
        return "Vehicle : " + self.vehicle.car_name + " | Quantity : " + str(self.quantity)

    # Total Price Method
    def total_price(self):
        return self.quantity * self.vehicle.car_price

class GroupMember(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    semester = models.IntegerField(default=3)
    personal_page = models.URLField()
    def __str__(self):
        return self.first_name
    class Meta:
        ordering = ['first_name']
