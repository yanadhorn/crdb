from django.conf import settings
from django.urls import path,include
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('chartjs/', views.chartjs, name='chartjs'),
    path('chartjs/', include('django.contrib.auth.urls')),
    path('person/', views.personlisting, name='personlist'),
    path('person/', include('django.contrib.auth.urls')),
]