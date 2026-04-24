from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('misiones/', views.misiones, name='misiones'), # <-- Asegúrate que diga name='misiones'
    path('recuerdos/', views.recuerdos, name='recuerdos'), # <-- Asegúrate que diga name='recuerdos'
]