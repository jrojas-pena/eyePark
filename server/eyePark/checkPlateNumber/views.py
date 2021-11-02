from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound
from .models import Car, Parking_Lot
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie, requires_csrf_token
import json
from django.contrib.auth.models import User
# Create your views here.

def checkPlateNumber(request):
    data = json.loads(request.body)
    parkingLot = get_object_or_404(Parking_Lot,pk=int(data['parking-lot-number']))
    car = get_object_or_404(Car, pk=data['license-plate'])
    print("Parking lot no: %d exist" % parkingLot.getNumber())
    print("Car with license plate: %s" % car)
    return HttpResponse()

def addPlateNumber(request):
    data = json.loads(request.body)
    parkingLot = get_object_or_404(Parking_Lot,pk=int(data['parking-lot-number']))
    user = parkingLot.user
    car = Car(user=user, license_plate=data['license-plate'])
    car.save()
    return HttpResponse()

@ensure_csrf_cookie
def giveCsrfToken(request):
    return HttpResponse()


