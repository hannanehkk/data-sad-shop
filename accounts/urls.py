from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('admin_register/', views.AdminRegister.as_view()),
    path('customer_register/', views.CustomerRegister.as_view()),
    path('login/', views.UserLogin.as_view()),
    path('logout/', views.UserLogout.as_view()),
]
