from django.shortcuts import render
from .models import Person
# Create your views here.
def persons(request):
    persons = Person.objects
    return render(request, 'persons/base.html', {'person': persons})