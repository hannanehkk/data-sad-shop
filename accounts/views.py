from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User, Admin, Customer
from .serializers import AdminRegisterSerializer, CustomerRegisterSerializer, UserSerializer, UserLoginSerializer
from rest_framework import status
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin


class AdminRegister(APIView):
    def post(self, request):
        pass


class CustomerRegister(APIView):
    def post(self, request):
        pass


class UserLogin(APIView):
    def post(self, request):
        pass


class UserLogout(LoginRequiredMixin, APIView):
    def get(self, request):
        pass