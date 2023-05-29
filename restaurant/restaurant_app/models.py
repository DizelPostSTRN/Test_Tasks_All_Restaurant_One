from django.db import models


class Meal(models.Model):
    name = models.CharField('Название блюда', max_length=100)
    description = models.TextField('Описание блюда')
    price = models.IntegerField('Стоимость блюда')
    size = models.IntegerField('Граммовка блюда')
    is_active = models.BooleanField('АКТИВНО', default=True)  # добавляем поле для активирования/деактивирования товара
    is_on_stop = models.BooleanField('НА СТОПЕ', default=False)  # добавляем поле для стоп-продажи товара

    def __str__(self):
        return self.name

    # class ProductAdmin(models.Model):
    #     fieldsets = (
    #         (None, {'fields': ('name', 'description', 'price')}),
    #         ('Availability', {'fields': ('is_active', 'is_on_stop'),  # добавляем поле is_on_stop в группу Availability
    #                             }),
    #     )

    class MealType(models.TextChoices):
        HOT_MEALS = 'Горячие блюда'
        DRINKS = 'Напитки'
        DESSERTS = 'Десерты'
        NO_TYPE = 'NO_TYPE'

    meal_type = models.CharField(
        'Категория блюда',
        max_length=30,
        choices=MealType.choices,
        default=MealType.NO_TYPE
    )


class MealClick(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.DO_NOTHING)
    click_date = models.DateTimeField('Дата клика')


# модель обработки аказов, которая будет связана с моделью Meal через отношение многие-ко-многим
class Order(models.Model):
    products = models.ManyToManyField(Meal)
    date_created = models.DateTimeField(auto_now_add=True)
