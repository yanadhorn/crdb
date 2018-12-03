from django.urls import path,include
from . import views

urlpatterns = [
    path('chartjs/', views.chartjs, name='chartjs'),
    path('chartjs/', include('django.contrib.auth.urls')),
    path('person/', views.personlisting, name='personlist'),
    path('person/', include('django.contrib.auth.urls')),
]