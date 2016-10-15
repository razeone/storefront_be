from rest_framework import serializers

from .models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = (
            'id',
            'email',
            'date_of_birth')
        extra_kwargs = {
            'users': {'lookup_field': 'email'}
        }
