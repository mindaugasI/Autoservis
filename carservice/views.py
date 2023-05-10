from django.shortcuts import render, get_object_or_404
from .models import *
from django.db.models import Q
from django.core.paginator import Paginator


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
    paginator = Paginator(CarModel.objects.all(), 2)
    page_number = request.GET.get('page')
    paged_cars = paginator.get_page(page_number)
    return render(request, 'cars.html', context={'cars': paged_cars})


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
    paginator = Paginator(OrderList.objects.all(), 1)
    page_number = request.GET.get('page')
    paged_orders = paginator.get_page(page_number)
    return render(request, 'orders.html', context={'orders': paged_orders})


def specific_order(request, order_list_id):
    order_list = get_object_or_404(OrderList, pk=order_list_id)
    orders_of_order_list = Order.objects.filter(Q(order_list_id__exact=order_list_id))
    context = {'order_list': order_list, 'orders': orders_of_order_list}
    return render(request, 'specific_order.html', context)


def search(request):
    """
    paprasta paieška. query ima informaciją iš paieškos laukelio,
    search_results prafiltruoja pagal įvestą automobilio modeli ir savininka.
    Icontains nuo contains skiriasi tuo, kad icontains ignoruoja ar raidės
    didžiosios/mažosios.
    """
    query = request.GET.get('query')
    search_results = Car.objects.filter(Q(car_model__car_model__icontains=query) | Q(client__icontains=query) |
                                         Q(plate_no__icontains=query) | Q(vin_number__icontains=query)
                                        | Q(car_model__brand__icontains=query))
    return render(request, 'search.html', {'cars': search_results, 'query': query})
