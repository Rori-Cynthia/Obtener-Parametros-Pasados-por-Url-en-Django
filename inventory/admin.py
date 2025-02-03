from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Manufacturer, Product, AccountUser


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'description', 'price', 'expiration_date', 'manufacturer'
    )
    list_filter = ('name', 'manufacturer',)
    list_per_page = 2


@admin.register(AccountUser)
class CustomUserAdmin(UserAdmin):
    model = AccountUser
    fieldsets = (
        ('User Data', {
            'fields': ('username', 'email', 'password')
        }),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'groups', 'user_permissions')
        }),
    )
    add_fieldsets = (
        ('User Data', {
            'fields': ('username', 'email', 'password1', 'password2')
        }),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'groups', 'user_permissions')
        }),
    )
