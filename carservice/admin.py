from django.contrib import admin
from .models import CarModel, Car, Service, ServicePrice, Order, OrderList

<<<<<<< HEAD
class OrderInline(admin.TabularInline):
    model = Order
    # turn off extra empty lines for inputs
    extra = 0

class OrderListAdmin(admin.ModelAdmin):
    list_display = ('car', 'order_date')
    inlines = [OrderInline]
=======

class OrderInline(admin.TabularInline):
    model = Order
    # Turn off extra empty lines for input
    extra = 0


class OrderListAdmin(admin.ModelAdmin):
    list_display = ('car', 'order_date')
    inlines = [OrderInline]


>>>>>>> 7211486ff028c2355969fff4557358f39cd6a75b

class CarAdmin(admin.ModelAdmin):
    list_display = ('client', 'plate_no', 'car_model', 'vin_number')
    list_filter = ('client', 'car_model')
    search_fields = ('plate_no', 'vin_number')

class ServicePriceAdmin(admin.ModelAdmin):
    list_display = ('service', 'price')

# Register your models here.
admin.site.register(CarModel)
admin.site.register(Car, CarAdmin)
admin.site.register(Service)
admin.site.register(ServicePrice)
admin.site.register(OrderList, OrderListAdmin)
admin.site.register(Order)
