from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Admin, Customer, User


class AdminProfileInline(admin.StackedInline):
    model = Admin
    can_delete = False


class CustomerProfileInline(admin.StackedInline):
    model = Customer
    can_delete = False


class ExtendedUserAdmin(UserAdmin):
    inlines = (AdminProfileInline, CustomerProfileInline)
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Added Fields',
            {
                "fields":
                    (
                        "type",
                    )
            },
        ),
    )


admin.site.register(User, ExtendedUserAdmin)
