from django.urls import path
from . import views
app_name = 'carapp'
urlpatterns = [
    path('', views.homepage, name='homepage'),
    #path('carapp/aboutus/', views.aboutus, name='aboutus'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('carapp/<int:cartype_no>/', views.cardetail, name='cartype_no'),
    #path('groupdetail/',views.groupdetail, name='groupdetails'),
    path('groupdetail/',views.GroupDetailView.as_view(), name='groupdetails'),
    path('carapp/vehicles/',views.vehicles, name='vehicles'),
    path('carapp/orderhere',views.orderhere , name='orderhere'),
    path('carapp/contact',views.contacts , name='groupcontact'),
    path('vehiclesearch/',views.VehicleSearch, name='vehiclesearch'),

    #path('carapp/contact_us',views.contact_us,name='contact_us'),
]
















































































