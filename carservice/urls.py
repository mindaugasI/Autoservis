from django.urls import path
from . import views


urlpatterns = [
    # Index
    path('', views.index, name='index'),
    # Page where all cars are displayed
    path('cars/', views.cars, name='cars'),
    path('cars/<int:car_id>', views.specific_car, name='specific_car'),
    path('services/', views.services, name='services'),
    path('orders/', views.orders, name='orders'),
    path('orders/<int:order_list_id>/', views.specific_order, name='specific_order'),
    path('search/', views.search, name='search'),
]