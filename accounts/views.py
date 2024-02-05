from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User, Admin, Customer
from .serializers import AdminRegisterSerializer, CustomerRegisterSerializer, UserSerializer, UserLoginSerializer
from rest_framework import status
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin


class AdminRegister(APIView):
    def post(self, request):
        ser_data = AdminRegisterSerializer(data=request.POST)
        if ser_data.is_valid():
            user = User.objects.create_user(username=ser_data.validated_data['username'],
                                            password=ser_data.validated_data['password'],
                                            email=ser_data.validated_data['email'],
                                            type=User.Types.ADMIN)
            Admin.objects.create(user=user, phoneNumber=ser_data.validated_data['phoneNumber'],
                                 id=ser_data.validated_data['id'])
            return Response(ser_data.data, status=status.HTTP_201_CREATED)
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomerRegister(APIView):
    def post(self, request):
        ser_data = CustomerRegisterSerializer(data=request.POST)
        if ser_data.is_valid():
            user = User.objects.create_user(username=ser_data.validated_data['username'],
                                            password=ser_data.validated_data['password'],
                                            email=ser_data.validated_data['email'],
                                            type=User.Types.CUSTOMER)
            Customer.objects.create(user=user, phoneNumber=ser_data.validated_data['phoneNumber'],
                                    city=ser_data.validated_data['city'])
            return Response(ser_data.data, status=status.HTTP_201_CREATED)
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLogin(APIView):
    def post(self, request):
        ser_data = UserLoginSerializer(data=request.POST)
        if ser_data.is_valid():
            user = authenticate(request, username=ser_data.validated_data['username'], password=ser_data.validated_data['password'])
            if user is not None:
                login(request, user)
                ser_data = UserSerializer(instance=user)
                return Response(ser_data.data, status=status.HTTP_200_OK)
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class UserLogout(LoginRequiredMixin, APIView):
    def get(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)
