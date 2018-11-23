from django.contrib import admin

# Register your models here. we can use appname.models also
from .models import person,education,education_grade,organization,org_categories,religions,address,contact,facebookAcc,twitterAcc,instagramAcc

class ReligionAdmin(admin.ModelAdmin):
    list_display = ('religion' , 'sect')
    search_fields = ('religion', 'sect')

class OrgInline(admin.TabularInline):
    model = organization
    extra = 1
    fk_name = 'organization_name'

class OrgCatAdmin(admin.ModelAdmin):
    list_display = ('org_categories',)

class OrgAdmin(admin.ModelAdmin):
    list_display = ('organization_name', 'org_address','org_categories','org_tel','org_field','org_mail','org_fund')
    search_fields = ('organization_name', 'org_address','org_categories','org_tel','org_field','org_mail','org_fund')

class EduInline(admin.TabularInline):
    model = education
    extra = 1
    fk_name = 'edu_name'

class EducationAdmin(admin.ModelAdmin):
    list_display = ('edu_name','edu_grade' )
    search_fields = ('edu_name','edu_grade')

class EduGradeAdmin(admin.ModelAdmin):
    list_display = ('edu_grade', 'edu_degree','edu_major' )
    search_fields = ('edu_grade', 'edu_degree','edu_major')

class contactInline(admin.TabularInline):
    model = contact
    extra = 2
    fk_name = 'personContact'

class facebookAccInline(admin.TabularInline):
    model = facebookAcc
    extra = 1
    fk_name = 'facebook'

class twitterAccInline(admin.TabularInline):
    model = twitterAcc
    extra = 1
    fk_name = 'twitter'

class instagramAccInline(admin.TabularInline):
    model = instagramAcc
    extra = 1
    fk_name = 'instagram'

class PersonAdmin(admin.ModelAdmin):
    list_display = ('name','surname','email')
    # search_fields = ('name','relation')
    # autocomplete_fields = ('religion','edu_name')
    inlines = [contactInline,EduInline,OrgInline,facebookAccInline,twitterAccInline,instagramAccInline]

class AddrAdmin(admin.ModelAdmin):
    list_display = ('addre','district','amphur','province')

admin.site.register(person,PersonAdmin)
admin.site.register(education,EducationAdmin)
admin.site.register(education_grade,EduGradeAdmin)
admin.site.register(organization,OrgAdmin)
admin.site.register(org_categories, OrgCatAdmin)
admin.site.register(religions, ReligionAdmin)
admin.site.register(address,AddrAdmin)