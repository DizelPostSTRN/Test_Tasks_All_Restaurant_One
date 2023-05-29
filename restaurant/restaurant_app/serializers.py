from rest_framework import serializers
from .models import Meal, Order


class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    products = MealSerializer(many=True)

    class Meta:
        model = Order
        fields = '__all__'

    def create(self, validated_data):
        products_data = validated_data.pop('products')
        order = Order.objects.create(**validated_data)
        for product_data in products_data:
            product = Meal.objects.get(id=product_data['id'])
            order.products.add(product)
        return order
