from django.db import models
from venues.models import Table


class Booking(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=255)
    booking_duration = models.IntegerField()
    booking_size = models.IntegerField()
    booking_date = models.DateField()
    booking_time = models.TimeField()
    booking_notes = models.TextField(null=True, blank=True)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.booking_date} {self.booking_time}"
