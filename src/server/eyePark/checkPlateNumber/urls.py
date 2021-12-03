from django.urls import path

from . import views

urlpatterns = [
    path('<int:parking_spot>/<str:license_plate>/', views.checkPlateNumber, name='check-plate'),
    path('add-plate/', views.addPlateNumber, name='add-plate')
]