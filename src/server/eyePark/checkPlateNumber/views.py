from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound
from .models import Car, Parking_Lot
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth.models import User
# Create your views here.

@csrf_exempt
def checkPlateNumber(request):
    data = json.loads(request.body)
    parkingLot = get_object_or_404(Parking_Lot,pk=int(data['parking-lot-number']))
    car = get_object_or_404(Car, pk=data['license-plate'])
    print("Parking lot no: %d exist" % parkingLot.getNumber())
    print("Car with license plate: %s" % car)
    return HttpResponse()

@csrf_exempt
def addPlateNumber(request):
    data = json.loads(request.body)
    parkingLot = get_object_or_404(Parking_Lot,pk=int(data['parking-lot-number']))
    user = parkingLot.user
    car = Car(user=user, license_plate=data['license-plate'])
    car.save()
    return HttpResponse()


