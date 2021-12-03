from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound
from .models import SecurityAlerts
from django.views.decorators.csrf import csrf_exempt
from django.template import loader
import json
from checkPlateNumber.models import Car, Parking_Lot

# Create your views here.

@csrf_exempt
def alertSecurity(request):
    data = json.loads(request.body)
    parking_spot = get_object_or_404(Parking_Lot, pk=data['parking-lot-number'])
    license_plate = data['license-plate']
    security_alert = SecurityAlerts(parking_spot = parking_spot, license_plate = license_plate)
    print(security_alert)
    security_alert.save()
    return HttpResponse()
    
def securityConfirmation(request):
    pass

def security(request):
    security_alerts_list = SecurityAlerts.objects.order_by('-id')
    template = loader.get_template('security/security.html')
    context = {
        'security_alerts_list' : security_alerts_list,
    }
    
    return HttpResponse(template.render(context, request))