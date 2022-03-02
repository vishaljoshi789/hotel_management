from django.db import models
from numpy import delete

# Create your models here.

class Booking(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, null=True)
    phone = models.CharField(max_length=100)
    checkin = models.DateField()
    checkout = models.DateField()
    room_no = models.IntegerField(unique=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    ac = models.BooleanField(default=False)
    wifi = models.BooleanField(default=False)

    def __str__(self):
        return self.name
