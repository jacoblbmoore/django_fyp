from django.contrib import admin
from .models import Booking
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'contact_number', 'booking_duration', 'booking_size', 'booking_date', 'booking_time', 'table')
