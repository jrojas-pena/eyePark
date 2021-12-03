from django.db import models
from django.db.models.deletion import CASCADE, DO_NOTHING

from checkPlateNumber.models import Parking_Lot, Car

# Create your models here.


class SecurityAlerts(models.Model):
    parking_spot = models.ForeignKey(Parking_Lot, on_delete=DO_NOTHING)
    license_plate = models.CharField(max_length=50)

    def __str__(self):
        return str(self.parking_spot) + " " + self.license_plate
        #self.license_plate

