from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Parking_Lot(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    number = models.IntegerField(default=0, primary_key=True)
    location = models.CharField(max_length=200)

    def getNumber(self):
        return self.number

    def __str__(self):
        return self.location + " " + str(self.number)

class Car(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    license_plate = models.CharField(max_length=15, primary_key=True)
    model = models.CharField(max_length=50)
    colour = models.CharField(max_length=10)

    def __str__(self):
        return self.license_plate
