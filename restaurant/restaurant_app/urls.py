from django.urls import path
from . import views

app_name = 'restaurant_app'

urlpatterns = [
    path('', views.menu, name='menu'),
    path('menu', views.menu, name='menu'),
    path('<meal_category>', views.meal_category, name='meal_category')
]