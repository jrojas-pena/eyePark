from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound
from .models import Car, Parking_Lot
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.

@csrf_exempt
def checkPlateNumber(request):
    data = json.loads(request.body)
    parkingLotNumber = get_object_or_404(Parking_Lot,pk=int(data['parking-lot-number']))
    licensePlate = get_object_or_404(Car, pk=data['license-plate'])
    print("Parking lot no: %d exist" % parkingLotNumber.getNumber())
    print("Car with license plate: %s" % licensePlate)
    return HttpResponse()

