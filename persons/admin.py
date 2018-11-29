from django.contrib import admin

# Register your models here. we can use appname.models also
from .models import title_name,person,jobs,education,education_grade,organization,org_categories,religions,address,personCoor,contact,facebookAcc,twitterAcc,instagramAcc

class ReligionAdmin(admin.ModelAdmin):
    list_display = ('religion' , 'sect')
    search_fields = ('religion', 'sect')

class OrgInline(admin.TabularInline):
    model = organization
    extra = 1
    # fk_name = 'organization_name'

class OrgCatAdmin(admin.ModelAdmin):
    list_display = ('org_categories',)

class OrgAdmin(admin.ModelAdmin):
    list_display = ('organization_name', 'org_address','org_categories','org_tel','org_field','org_mail','org_fund')
    search_fields = ('organization_name', 'org_address','org_categories','org_tel','org_field','org_mail','org_fund')

class EduInline(admin.TabularInline):
    model = education
    extra = 1
    fields = ('edu_name','edu_grade')
    # fk_name = 'edu_name'

class EducationAdmin(admin.ModelAdmin):
    list_display = ('edu_name','edu_grade' )
    search_fields = ('edu_name','edu_grade')

class EduGradeAdmin(admin.ModelAdmin):
    list_display = ('edu_grade', 'edu_degree','edu_major' )
    search_fields = ('edu_grade', 'edu_degree','edu_major')

class contactAdmin(admin.ModelAdmin):
    list_display = ('contactType', 'phonenumber')

class contactInline(admin.TabularInline):
    model = contact
    extra = 1
    fk_name = 'personContact'

class facebookAccAdmin(admin.ModelAdmin):
    fields = ('facebook',)

class facebookAccInline(admin.TabularInline):
    model = facebookAcc
    extra = 1
    # fk_name = 'facebook'

class twitterAccAdmin(admin.ModelAdmin):
    list_display = ('twitter',)

class twitterAccInline(admin.TabularInline):
    model = twitterAcc
    extra = 1
    # fk_name = 'twitter'

class instagramAccAdmin(admin.ModelAdmin):
    display = ('instagram')

class instagramAccInline(admin.TabularInline):
    model = instagramAcc
    extra = 1
    # fk_name = 'instagram'

class titleAdmin(admin.ModelAdmin):
    list_display = ('title_short','title_full')
    search_fields = ('title_short','title_full')
    # autocomplete_fields = ('title_short',)

class AddrInlineAdmin(admin.TabularInline):
    model = address
    extra = 1

class jobsInlineAdmin(admin.TabularInline):
    model = jobs
    extra = 1

class jobsAdmin(admin.ModelAdmin):
    list_display = ('job','job_description')
    search_fields = ('job','job_description')

class PersonAdmin(admin.ModelAdmin):
    list_display = ('name','surname','email')
    search_fields = ('name','nickname')
    autocomplete_fields = ('title_short','religion')
    # inlines = [AddrInlineAdmin]
    inlines = [AddrInlineAdmin,contactInline,jobsInlineAdmin,EduInline,OrgInline,facebookAccInline,twitterAccInline,instagramAccInline]

class AddrAdmin(admin.ModelAdmin):
    list_display = ('addre','district','amphur','province')

# class profilesAdmin(admin.ModelAdmin):
#     list_display = ('name','surname','email')
#     search_fields = ('name','nickname')
#     autocomplete_fields = ('title_short','religion')
#     inlines = [contactInline,EduInline,OrgInline,facebookAccInline,twitterAccInline,instagramAccInline]

# admin.site.register(profiles,profilesAdmin)
admin.site.register(title_name,titleAdmin)
admin.site.register(person,PersonAdmin)
admin.site.register(contact,contactAdmin)
admin.site.register(education,EducationAdmin)
admin.site.register(education_grade,EduGradeAdmin)
admin.site.register(organization,OrgAdmin)
admin.site.register(org_categories, OrgCatAdmin)
admin.site.register(religions, ReligionAdmin)
admin.site.register(jobs,jobsAdmin)
admin.site.register(address, AddrAdmin)
admin.site.register(facebookAcc, facebookAccAdmin)
admin.site.register(twitterAcc,twitterAccAdmin)
admin.site.register(instagramAcc,instagramAccAdmin)