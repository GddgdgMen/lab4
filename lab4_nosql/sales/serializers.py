from rest_framework import serializers
from .models import Salesperson

class SalespersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Salesperson
        fields = ['id', 'code', 'full_name', 'age', 'gender', 'phone_number', 'date_joined']


class SalespersonUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Salesperson
        # Only allow these fields to be updated
        fields = ['full_name', 'age', 'phone_number']
