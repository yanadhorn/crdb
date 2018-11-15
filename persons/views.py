from django.shortcuts import render
from persons.models import person
# Create your views here.
def persons(request):
    persons = person.objects
    return render(request, 'persons/base.html', {'person': persons})