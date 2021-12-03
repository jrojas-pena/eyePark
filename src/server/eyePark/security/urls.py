from django.urls import path

from . import views

urlpatterns = [
    path('', views.security, name='security'),
    path('alert/', views.alertSecurity, name='alert'),
    path('confirmation/', views.securityConfirmation, name='confirmation')
]