from rest_framework import serializers
from .models import User, Admin, Customer


class AdminRegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Admin
        fields = ('username', 'password', 'password2', 'email', 'phoneNumber', 'id')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate_username(self, value):
        if value == 'admin':
            raise serializers.ValidationError('username cant be `admin`')
        return value

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError('passwords must match')
        return data


class CustomerRegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Customer
        fields = ('username', 'password', 'password2', 'email', 'phoneNumber', 'city')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate_username(self, value):
        if value == 'admin':
            raise serializers.ValidationError('username cant be `admin`')
        return value

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError('passwords must match')
        return data


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('username', 'password')
