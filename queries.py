import django
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'carsite.settings')
django.setup()
from carapp.models import CarType, Vehicle, Buyer, OrderVehicle

option = int(input("Enter query Number"))

