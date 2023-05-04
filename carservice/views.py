from django.shortcuts import render, get_object_or_404
from .models import *


def index(request):
    car_models = CarModel.objects.all()
    car_model_count = CarModel.objects.count()
    services = Service.objects.all()
    services_count = Service.objects.count()

    context = {
        'car_models': car_models,
        'car_model_count': car_model_count,
        'services': services,
        'services_count': services_count,
    }
    return render(request, "index.html", context)

def cars(request):
    all_cars = CarModel.objects.all()
    context = {
        'cars': all_cars
    }
    return render(request, "cars.html", context)

def specific_car(request, car_id):
    car = Car.objects.get(car_id=car_id)
    context = {'car': car}
    return render(request, "specific_car.html", context)


def services(request):
    all_services = Service.objects.all()
    context = {
        'services': all_services
    }
    return render(request, "services.html", context)

def orders(request):
    all_orders = OrderList.objects.all()
    context = {
        'orders': all_orders
    }
    return render(request, 'orders.html', context)

def specific_order(request, order_id):
    pass
