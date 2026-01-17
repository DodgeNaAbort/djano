from rest_framework import serializers
from django.utils import timezone
from datetime import date

NAME_FIELD_KWARGS = {
    'max_length': 30,
    'trim_whitespace': True,
    'allow_blank': False,
    'required': True
}

class UserSerializer(serializers.Serializer):
    first_name = serializers.CharField(
        **NAME_FIELD_KWARGS
    )
    last_name = serializers.CharField(
        **NAME_FIELD_KWARGS
    )
    patronymic = serializers.CharField(
        **NAME_FIELD_KWARGS
    )
    email = serializers.EmailField(
        **NAME_FIELD_KWARGS
    )
    password = serializers.CharField(
        min_length = 3,
        **NAME_FIELD_KWARGS
    )
    birth_date = serializers.DateField(
        allow_null = False,
        required = True
    )
    
    def validate_first_name(self, value):
        if not value[0].isupper():
            raise serializers.ValidationError("First name must start with a capital letter")
        
        return value
    
    def validate_last_name(self, value):
        if not value[0].isupper():
            raise serializers.ValidationError("Last name must start with a capital letter")
        
        return value
    
    def validate_patronymic(self, value):
        if not value[0].isupper():
            raise serializers.ValidationError("Patronymic must start with a capital letter")
        
        return value
    
    def validate_birth_date(self, value):
        today = timezone.now().date()
        
        if value > today:
            raise serializers.ValidationError("Birth date cannot be in the future")
        
        if value < date(1900, 1, 1):
            raise serializers.ValidationError("Birth date cannot be earlier than 1900-01-01")
        
        return value
    
    def validate_email(self, value):
        if not value or not value.strip():
            raise serializers.ValidationError("Email is required")
        
    def validate_password(self, value):
        if not any(c.isupper() for c in value) or not any(c.islower() for c in value) or not any(c.isdigit() for c in value):
            raise serializers.ValidationError('Password is invalid')