from django import forms
from venues.models import Section, Table  # Import Table as well


class SectionForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = ['name', 'booking_priority']


class TableForm(forms.ModelForm):
    class Meta:
        model = Table
        fields = ['name', 'min_seats', 'max_seats']
