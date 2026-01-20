from rest_framework import serializers
from .models import User  
from django.utils import timezone
from datetime import date

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'patronymic', 
                 'email', 'password', 'birth_date']
        extra_kwargs = {
            'password': {'write_only': True, 'min_length': 3},
            'email': {'required': True},
            'first_name': {'required': True, 'max_length': 30},
            'last_name': {'required': True, 'max_length': 30},
            'patronymic': {'required': True, 'max_length': 30},
        }
    
    def validate_first_name(self, value):
        if not value[0].isupper():
            raise serializers.ValidationError("First name must start with a capital letter")
        return value
    
    def validate_birth_date(self, value):
        today = timezone.now().date()
        if value > today:
            raise serializers.ValidationError("Birth date cannot be in the future")
        if value < date(1900, 1, 1):
            raise serializers.ValidationError("Birth date cannot be earlier than 1900-01-01")
        return value