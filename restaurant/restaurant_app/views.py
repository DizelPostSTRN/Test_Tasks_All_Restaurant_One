from django.shortcuts import render
from .models import Meal
from django.utils import timezone

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

