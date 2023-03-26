from django.db import models
from django.contrib.auth.models import User


class Venue(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    address = models.TextField()

    def __str__(self):
        return self.name


class Section(models.Model):
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    booking_priority = models.IntegerField()

    def __str__(self):
        return self.name


class Table(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    min_seats = models.IntegerField()
    max_seats = models.IntegerField()

    def __str__(self):
        return self.name


class TableCombination(models.Model):
    tables = models.ManyToManyField(Table)
    min_combined_capacity = models.IntegerField()
    max_combined_capacity = models.IntegerField()

    def __str__(self):
        return f"Combination {self.pk}"
