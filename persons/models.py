from django.db import models
from django.core.validators import URLValidator

# Create your models here.
# ประเภทขององค์กร รัฐ เอกชน สังคม
class org_categories(models.Model):
    org_categories = models.CharField(max_length=255)

    def __str__(self):
        return self.org_categories

#ระดับชั้นการศึกษา ปริญญา สาขา เอก
class education_grade(models.Model):
    edu_grade = models.CharField(null=True,max_length=200)
    edu_degree = models.CharField(blank=True,null=True,max_length=200)
    edu_major = models.CharField(blank=True,null=True,max_length=200)

    def __str__(self):
        return self.edu_grade

#ศาสนา และนิกาย
class religions(models.Model):
    religion = models.CharField(max_length=255)
    sect = models.CharField(blank=True,null=True,max_length=255)

    def __str__(self):
        return u'%s: %s'% (self.religion,self.sect)

class address(models.Model):
    addre = models.CharField(blank=True,null=True,max_length=255)
    district = models.CharField(null=True,max_length=255)
    amphur = models.CharField(null=True,max_length=255)
    province = models.CharField(max_length=255)

    def __str__(self):
        return u'%s: %s %s %s'% (self.addre,self.district,self.amphur,self.province)

class person(models.Model):
    sex = (
        ('male', 'ผู้ชาย'),
        ('female', 'ผู้หญิง'),
    )
    title_name = (
        ('mr', 'นาย'),
        ('mrs', 'นาง'),
        ('ms', 'นางสาว'),
        ('dr','ดร.'),
        ('Asst','ผศ.'),
        ('Asst Dr','ผศ. ดร.'),
        ('ML','มล.')
    )
    status_list = (
        ('single','โสด'),
        ('married','แต่งงาน'),
        ('divorce','หย่าร้าง'),
        ('complicated','ซับซ้อน'),
    )
    person_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, choices=title_name)
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    nickname = models.CharField(blank=True,null=True,max_length=100)
    sex_status = models.CharField(max_length=255, choices=sex)
    religion = models.ForeignKey(religions,blank=True,null=True,on_delete=models.CASCADE)
    status = models.CharField(max_length=100,choices=status_list)
    image = models.ImageField(blank=True,upload_to='images/')
    email = models.EmailField(blank=True,null=True,max_length=255)
    dob = models.DateField(blank=True,null=True)
    addre = models.ForeignKey(address,blank=True,null=True,on_delete=models.CASCADE)
    latCo = models.CharField(blank=True,null=True,max_length=255)
    longCo = models.CharField(blank=True,null=True,max_length=255)
    relation = models.CharField(blank=True,null=True,max_length=255)
    friends = models.ManyToManyField("self",blank=True)
    job = models.CharField(blank=True,null=True,max_length=255)
    job_description = models.TextField(blank=True,null=True)
    remark = models.TextField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = models.Manager()
    
    def __str__(self):
        return self.name

class contact(models.Model):
    phoneType = (
        ('Home','บ้าน'),
        ('Work','ที่ทำงาน'),
        ('Mobile','มือถือ'),
        ('Mobile2','มือถือ2'),
    )
    personContact = models.ForeignKey(person,blank=True,null=True,on_delete=models.CASCADE)
    contactType = models.CharField(max_length=100,choices=phoneType)
    phonenumber = models.IntegerField()

class organization(models.Model):
    # org_id = models.AutoField(primary_key=True)
    organization_name = models.ForeignKey(person,on_delete=models.CASCADE,max_length=255)
    org_address = models.CharField(max_length=255)
    org_categories = models.ForeignKey(org_categories,on_delete=models.CASCADE)
    org_website = models.URLField(blank=True,null=True)
    org_tel = models.CharField(blank=True,null=True,max_length=255)
    org_field = models.CharField(blank=True,null=True,max_length=255)
    org_mail = models.EmailField(blank=True,null=True,max_length=255)
    org_fund = models.CharField(blank=True,null=True,max_length=255)

    def __str__(self):
        return self.organization_name

#ชื่อมหาลัย ระดับชั้นการศึกษา
class education(models.Model):
    edu_name = models.ForeignKey(person,on_delete=models.DO_NOTHING)
    edu_grade = models.ForeignKey(education_grade,on_delete=models.CASCADE)

    def __str__(self):
        return self.edu_name

#บัญชี social media
class facebookAcc(models.Model):
    facebook = models.ForeignKey(person,validators=URLValidator,on_delete=models.CASCADE,blank=True,null=True,max_length=255)

    def __str__(self):
        return self.facebook

class twitterAcc(models.Model):
    twitter = models.ForeignKey(person,validators=URLValidator,on_delete=models.CASCADE,blank=True,null=True,max_length=255)
    instagram = models.ForeignKey(person,validators=URLValidator,on_delete=models.CASCADE,blank=True,null=True,max_length=255)

    def __str__(self):
        return self.twitter

class instagramAcc(models.Model):
    instagram = models.ForeignKey(person,validators=URLValidator,on_delete=models.CASCADE,blank=True,null=True,max_length=255)

    def __str__(self):
        return self.instagram

# class relations(models.Model):
#     relations_type = (
#         ('father', 'พ่อ'),
#         ('mother', 'แม่'),
#         ('son', 'ลูกชาย'),
#         ('daugther','ลูกสาว'),
#         ('aunt','ป้า'),
#         ('olderbrother','พี่ชาย'),
#         ('littlebrother','น้องชาย'),
#         ('oldersister','พี่สาว'),
#         ('littlesister','น้องสาว'),
#     )
#     relation = models.CharField(max_length=100, choices=relations_type)
#     person1 = models.ForeignKey(person,on_delete=models.DO_NOTHING)
