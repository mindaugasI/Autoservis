from django.contrib import admin
from .models import CarModel, Car, Service, ServicePrice, Order

class CarAdmin(admin.ModelAdmin):
    list_display = ('client', 'plate_no', 'car_model', 'vin_number')
    list_filter = ('client', 'car_model')
    search_fields = ('plate_no', 'vin_number')

# Register your models here.
admin.site.register(CarModel)
admin.site.register(Car, CarAdmin)
admin.site.register(Service)
admin.site.register(ServicePrice)
admin.site.register(Order)
#admin.site.register(OrderList)