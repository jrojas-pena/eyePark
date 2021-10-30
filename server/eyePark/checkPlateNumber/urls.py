from django.urls import path

from . import views

urlpatterns = [
    path('', views.checkPlateNumber, name='check-plate-number'),
]