from django.contrib import admin
from trip.models import Airport, Company, Pass_in_trip, Plane, Trip


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    # list_display = ('__all__',)
    # search_fields = ('username', 'email')
    empty_value_display = '-пусто-'
    # list_filter = ('username', 'email')

@admin.register(Airport)
class AirportAdmin(admin.ModelAdmin):
    empty_value_display = '-пусто-'

@admin.register(Pass_in_trip)
class Pass_in_tripAdmin(admin.ModelAdmin):
    empty_value_display = '-пусто-'

@admin.register(Plane)
class PlaneAdmin(admin.ModelAdmin):
    empty_value_display = '-пусто-'

@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    empty_value_display = '-пусто-'
