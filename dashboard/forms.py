from django import forms
from venues.models import Section, Table  # Import Table as well
from bookings.models import Booking


class SectionForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = ['name', 'booking_priority']


class TableForm(forms.ModelForm):
    class Meta:
        model = Table
        fields = ['name', 'min_seats', 'max_seats']


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [
            'first_name',
            'last_name',
            'contact_number',
            'booking_size',
            'booking_date',
            'booking_time',
            'booking_notes',
        ]
        widgets = {
            'booking_date': forms.DateInput(attrs={'type': 'date'}),
            'booking_time': forms.TimeInput(attrs={'type': 'time'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        booking_size = cleaned_data.get('booking_size')

        if booking_size:
            if booking_size > 8:
                cleaned_data['booking_duration'] = 3
            else:
                cleaned_data['booking_duration'] = 2

        return cleaned_data

