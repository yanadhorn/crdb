from django.contrib import admin

# Register your models here. we can use appname.models also
from .models import person,education,education_grade,organization,org_categories,religions,address,contact

class ReligionAdmin(admin.ModelAdmin):
    list_display = ('religion' , 'sect')
    search_fields = ('religion', 'sect')

# class BookAdmin(admin.ModelAdmin):
#     list_display = ('title', 'publisher', 'publication_date')
#     list_filter = ('publication_date',)

class OrgCatAdmin(admin.ModelAdmin):
    list_display = ('org_categories',)

class EducationAdmin(admin.ModelAdmin):
    list_display = ('edu_id', 'edu_name','edu_grade' )
    search_fields = ('edu_name','edu_grade')

class OrgAdmin(admin.ModelAdmin):
    list_display = ('organization_name', 'org_address','org_categories','org_tel','org_field','org_mail','org_fund')
    search_fields = ('organization_name', 'org_address','org_categories','org_tel','org_field','org_mail','org_fund')

class EduGradeAdmin(admin.ModelAdmin):
    list_display = ('edu_grade', 'edu_degree','edu_major' )
    search_fields = ('edu_grade', 'edu_degree','edu_major')

class contactInline(admin.TabularInline):
    model = contact
    extra = 4
    fk_name = 'personContact'

class PersonAdmin(admin.ModelAdmin):
    list_display = ('name','surname','email', 'mobiles')
    # search_fields = ('name','relation')
    # autocomplete_fields = ('religion','edu_name')
    inlines = [contactInline,]

class AddrAdmin(admin.ModelAdmin):
    list_display = ('addre','district','amphur','province')

# class contactAdmin(admin.ModelAdmin):
#     list_display = ('contactType','phonenumber')
#     inlines = [contactInline]

admin.site.register(person,PersonAdmin)
admin.site.register(education,EducationAdmin)
admin.site.register(education_grade,EduGradeAdmin)
admin.site.register(organization,OrgAdmin)
admin.site.register(org_categories, OrgCatAdmin)
admin.site.register(religions, ReligionAdmin)
admin.site.register(address,AddrAdmin)
# admin.site.register(contact,contactAdmin)