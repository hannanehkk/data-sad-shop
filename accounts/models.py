from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    class Types(models.IntegerChoices):
        ADMIN = 1
        CUSTOMER = 2

    type = models.IntegerField(choices=Types.choices, default=Types.CUSTOMER)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=256, blank=True, null=True)
    password = models.CharField(max_length=256, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phoneNumber = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.user.username

    class Meta:
        abstract = True


class Admin(Profile):
    id = models.DecimalField(max_digits=2, decimal_places=0, primary_key=True, unique=True)


class Customer(Profile):
    city = models.TextField(max_length=256, blank=True, null=True)
