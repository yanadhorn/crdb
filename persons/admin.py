from django.contrib import admin

# Register your models here.
from .models import person,education,education_grade,organization,org_categories,religions

admin.site.register(person)
admin.site.register(education)
admin.site.register(education_grade)
admin.site.register(organization)
admin.site.register(org_categories)
admin.site.register(religions)