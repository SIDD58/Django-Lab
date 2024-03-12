from urllib import response

from django.http import HttpResponse
# This is Relative import used within a package
from .models import Vehicle, CarType, Buyer,OrderVehicle, GroupMember
from django.shortcuts import get_object_or_404,get_list_or_404,render
from django.views import View
from .forms import ContactForm,OrderVehicleForm,VehicleSearchForm

from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import FormView






# def homepage(request):
#     cartype_list=CarType.objects.all().order_by('-vehicles__car_price')[:10]
#     response= HttpResponse()
#     heading1='<p>'+'Different Types of Cars:'+'</p>'
#     response.write(heading1)
#     for cartype in cartype_list:
#         para='<p>'+ str(cartype.id)+'</p>'
#         response.write(para)
#     return response
def homepage(req):
    cartype_list=CarType.objects.all().order_by('id')
    return render(req,'carapp/homepage.html',{'cartype_list':cartype_list})

def vehicles(req):
    form =OrderVehicleForm()
    vehicles_all=Vehicle.objects.all()
    return render(req,'carapp/vehicles.html',{'form': form,'vehicles_all':vehicles_all})

def contacts(req):
    form =ContactForm()
    return render(req,'carapp/contact.html',{'form': form})

#EXTRA VARAIBLE : cartype_list object is passed as a context variable
def aboutus(request):
    return render(request, 'carapp/aboutus.html')

# NO extra content variable needs to be passed


#Class Based View
# class AboutUsView(View):
#     content = "<p>This is a Car Showroom</p>"
#     def get(self, request):
#         return HttpResponse(self.content)

# def cardetail(request,cartype_no):
#     #cartype=CarType.objects.get(id=cartype_no)
#     cartype=get_object_or_404(CarType, id=cartype_no)
#     vehicles=Vehicle.objects.filter(car_type__name=cartype.name)
#     response = HttpResponse()
#     for vehicle in vehicles:
#         para="<p>"+ vehicle.car_name
#         response.write(para)
#     return response

def cardetail(request,cartype_no):
    cartype = get_object_or_404(CarType, id=cartype_no)
    vehicles=Vehicle.objects.filter(car_type__id=cartype_no)
    return render(request, 'carapp/cardetail.html',{'cartype':cartype,'vehicles':vehicles})


def orderhere(request):
    res=HttpResponse()
    res.write("You can place your order here.")
    return res


def VehicleSearch(request):
    if request.method=='GET':
        vehicle = Vehicle.objects.all()
        form = VehicleSearchForm()
        return render(request, 'carapp/vehicle_search.html', { 'form': form})
    else:
        form = VehicleSearchForm(request.POST)
        if form.is_valid():
            result_string='Your Search Result'
            car_name=form.cleaned_data.get('car_name')
            car_price=None
            vehicle = Vehicle.objects.get(car_name=car_name)
            car_price=vehicle.car_price
            return render(request, 'carapp/vehicle_search.html', {'car_price':car_price, 'form': form,'result_string':result_string})

def orderhere(request):
    msg=''
    vehiclelist=Vehicle.objects.all()
    if request.method == 'POST':
        form = OrderVehicleForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            if order.quantity <= order.vehicle.inventory:
                order.vehicle.inventory -= order.quantity
                order.vehicle.save()
                order.save()
                msg= ('Your Vehicle has been ordered')
            else:
                msg='We do not have suffienceint stock to fill you order'
                return render(request,'carapp/nosuccess_order.html',{'msg':msg})
    else:
        form = OrderVehicleForm()
    return render(request, 'carapp/orderhere.html',{'form':form,'msg':msg,'vehiclelist':vehiclelist})











# def groupdetail(request):
#     members = GroupMember.objects.all().order_by('first_name')
#     response = HttpResponse()
#     for member in members:
#         heading=("<h3>"+member.first_name+"</h3>")
#         response.write(heading)
#         para=("<p>"
#               + member.first_name + "<br>"
#               + member.last_name + "<br>"
#               + str(member.semester) + "<br>"
#               + member.personal_page + "<br>"
#               "</p>")
#         response.write(para)
#     return response

class GroupDetailView(View):
    def get(self,req):
        members = GroupMember.objects.all().order_by('first_name')
        return render(req, 'carapp/group-detail.html', {'members': members})




# def groupdetail(request):
#     print("HI")
#     members = GroupMember.objects.all().order_by('first_name')
#     response = HttpResponse()
#     for member in members:
#         heading=("<h3>"+member.first_name+"</h3>")
#         response.write(heading)
#         para=("<p>"
#               + member.first_name + "<br>"
#               + member.last_name + "<br>"
#               + str(member.semester) + "<br>"
#               + member.personal_page + "<br>"
#               "</p>")
#         response.write(para)
#     return response
# def contact_us(request):
#     para="<p>"+"Contact us at the following number : 9872007008 "+"</p>"
#     res=HttpResponse()
#     res.write(para)
#     return res














# Difference between FBV and CBV

# a) Class Based Views -> we need to import View from django.views and inherit View
# UNLIKE function based views
# b) Class based views -> we need to mention the request method
# UNLIKE function based views
# c)Class based views -> we need to use as_view() method in urls.py
# UNLIKE function based views
# Explanation : # URL dispatcher expects function as_view creates instance of class based view and determines
# appropriate HTTP handler in the view class if it exist else returns 405 method not allowed

# Pros Of Class Based Views
# class based views we do not have to use branching for different request methods like in function based views
# class based views improves reusability and seperation of concerns as they are
# Class based Views we can share variable among different request methods using class variables

































































