from django.shortcuts import render
from .models import Meal

def menu(request):
    meal_categories = list(filter(lambda el: 'NO_TYPE' not in el[0], Meal.MealType.choices))
    return render(request, 'restaurant_app/menu.html', {'meal_categories': meal_categories})


def meal_category(requset, meal_category):
    pass
