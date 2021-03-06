from django.contrib import admin
from .models import (
    Car, CarShowroom,
    ShowroomSellCar, Customer,
    Transaction, Supplier,
    SupplierSellCar
)


# Register your models here.
@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = (
        'brand',
        'image',
        'max_speed',
        'engine_power',
        'mileage',
        'description',
    )
    list_filter = (
        'max_speed',
        'mileage',
    )


@admin.register(CarShowroom)
class CarShowroomAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'balance',
    )
    list_filter = (
        'name',
    )


@admin.register(ShowroomSellCar)
class ShowroomSellCarAdmin(admin.ModelAdmin):
    list_display = (
        'car',
        'showroom',
        'count',
        'price',
        'supplier',
    )
    list_filter = (
        'count',
        'price',
    )


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'age',
        'balance',
    )
    list_filter = (
        'first_name',
        'age',
    )


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = (
        'price',
        'count',
        'car',
        'car_showroom',

    )
    list_filter = (
        'price',
        'count',
    )


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'date_of_creation',
    )
    list_filter = (
        'name',
        'date_of_creation',
    )


@admin.register(SupplierSellCar)
class SupplierSellCar(admin.ModelAdmin):
    list_display = (
        'car',
        'supplier',
        'price',
    )
    list_filter = (
        'price',
    )
