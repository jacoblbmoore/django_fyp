from django.contrib import admin
from .models import Venue, Section, Table, TableCombination

@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'name', 'address')

@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'venue', 'name', 'booking_priority')

@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ('id', 'section', 'name', 'min_seats', 'max_seats')

@admin.register(TableCombination)
class TableCombinationAdmin(admin.ModelAdmin):
    list_display = ('id', 'min_combined_capacity', 'max_combined_capacity')

