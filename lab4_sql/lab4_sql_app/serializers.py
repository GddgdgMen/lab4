from rest_framework import serializers
from .models import Client, Product, Order


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'name', 'age', 'gender', 'type', 'price']


class ClientUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        # Only allow these fields to be updated
        fields = ['name', 'age', 'gender', 'type', 'price']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        extra_kwargs = {
            'price': {'min_value': 0.00}
        }
        fields = ['id', 'type', 'price']


class ProductUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        # Only allow these fields to be updated
        extra_kwargs = {
            'price': {'min_value': 0.00}
        }
        fields = ['type', 'price']


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'client', 'product']

    def to_representation(self, instance):
        self.fields['client'] = ClientSerializer(read_only=True)
        self.fields['product'] = ProductSerializer(read_only=True)
        return super().to_representation(instance)


class OrderUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        # Only allow these fields to be updated
        fields = ['client', 'product']
