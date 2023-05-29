from django.urls import path
from . import views
from .views import OrderListCreateView
from .views import create_order, get_orders

app_name = 'restaurant_app'

urlpatterns = [
    path('', views.menu, name='menu'),
    path('menu', views.menu, name='menu'),
    path('<meal_category>', views.meal_category, name='meal_category'),
    path('<int:meal_id>/meal', views.meal, name='meal'),
    path('orders/', OrderListCreateView.as_view(), name='order-list-create'),
    path('orders/', get_orders, name='get_orders'),
    path('orders/create/', create_order, name='create_order'),
]
