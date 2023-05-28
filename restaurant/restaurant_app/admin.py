from django.contrib import admin
from .models import Meal


class ProductAdmin(admin.ModelAdmin):
    list_display = ['meal_type', 'name', 'price', 'description', 'is_active',
                    'is_on_stop']  # добавляем поле is_on_stop в список отображаемых полей
    list_filter = ['is_active', 'is_on_stop']  # добавляем фильтр по полю is_on_stop


admin.site.register(Meal, ProductAdmin)
