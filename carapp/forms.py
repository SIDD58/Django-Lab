from django import forms
from .models import OrderVehicle,Vehicle

class OrderVehicleForm(forms.ModelForm):
    class Meta:
        model = OrderVehicle
        fields=['vehicle','buyer','quantity']
        widgets = {
            'buyer': forms.Select(),  # Corrected to use Select for single selection
        }
        labels = {
            'quantity': 'Vehicle_Ordered',  # Setting a custom label for 'quantity'
        }

class ContactForm(forms.Form):
    ID=forms.IntegerField()
    name = forms.CharField(max_length=30)
    email=forms.EmailField()
    subject=forms.CharField(max_length=30)
    reason= forms.CharField(widget=forms.Textarea)
    message=forms.CharField(widget=forms.Textarea)

class VehicleSearchForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        vehicle = Vehicle.objects.all()
        result = [(i, i) for i in vehicle]
        fields=['car_name']
        widgets={'car_name':forms.Select(choices=result)}

# class VehicleSearchForm(forms.Form):
#     vehicle = Vehicle.objects.all()
#     result = [(i, i) for i in vehicle]
#     car_name = forms.CharField(widget=forms.Select(choices=result))







