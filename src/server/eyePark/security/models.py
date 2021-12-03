from django.db import models
from django.db.models.deletion import CASCADE, DO_NOTHING

from checkPlateNumber.models import Parking_Lot, Car

# Create your models here.


class SecurityAlerts(models.Model):
    parking_spot = models.ForeignKey(Parking_Lot, on_delete=DO_NOTHING)
    license_plate = models.ForeignKey(Car, on_delete=DO_NOTHING)

    def __str__(self):
        self.parking_spot + " " + self.license_plate

