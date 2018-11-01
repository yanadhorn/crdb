from django.contrib import admin

# Register your models here.
from .models import Person,education,education_grade,organization

admin.site.register(Person)
admin.site.register(education)
admin.site.register(education_grade)
admin.site.register(organization)