from django.urls import path

from . import views

urlpatterns = [
    path('<int:parking-spot>/<string:license-plate>/', views.checkPlateNumber, name='check-plate'),
    path('add-plate/', views.addPlateNumber, name='add-plate')
]