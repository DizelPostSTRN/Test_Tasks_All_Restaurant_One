from django.shortcuts import render
from .models import Meal
from django.utils import timezone
from django.http import JsonResponse
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Order
from .serializers import OrderSerializer


def menu(request):
    meal_categories = list(filter(lambda el: 'NO_TYPE' not in el[0], Meal.MealType.choices))
    return render(request, 'restaurant_app/menu.html', {'meal_categories': meal_categories})


def meal_category(request, meal_category):
    meals_by_category = Meal.objects.filter(meal_type=meal_category)
    return render(request, 'restaurant_app/meals.html', {'meals': meals_by_category, 'meal_category': meal_category})


def meal(request, meal_id):
    meal = Meal.objects.get(id=meal_id)
    meal.mealclick_set.create(click_date=timezone.now())
    return render(request, 'restaurant_app/meal.html', {'meal': meal})


# meal.mealclick_set.create(click_date=timezone.now) - Добавляем статисктику по кликам при
# переходе на каждую страничку
# (ссылаемся на класс class MealClick из models, меняем регистр на маленький)
# mealclick_set что бы менять данные в моделях
# По сути будет создаваться объект с датой когда пользователь нажал на какое нибудь блюдо

def statistics():
    pass


class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


def create_order(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        products = [Meal.objects.get(id=product['id']) for product in data['products']]
        order = Order.objects.create()
        order.products.add(*products)
        order.save()
        return JsonResponse({'status': 'created'})
    else:
        return JsonResponse({'error': 'invalid method'})


def get_orders(request):
    if request.method == 'GET':
        orders = Order.objects.all().order_by('-date_created')
        data = [
            {'id': order.id, 'products': [{'id': product.id, 'name': product.name} for product in order.products.all()]}
            for order in orders]
        return JsonResponse({'orders': data})
    else:
        return JsonResponse({'error': 'invalid method'})
