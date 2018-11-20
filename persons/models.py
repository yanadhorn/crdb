from django.db import models

# Create your models here.
# ประเภทขององค์กร รัฐ เอกชน สังคม
class org_categories(models.Model):
    org_categories = models.CharField(max_length=255)

#รายชื่อองค์กร
class organization(models.Model):
    # org_id = models.AutoField(primary_key=True)
    organization_name = models.CharField(max_length=255)
    org_address = models.CharField(max_length=255)
    org_categories = models.ForeignKey(org_categories,on_delete=models.CASCADE)
    org_tel = models.CharField(blank=True,null=True,max_length=255)
    org_field = models.CharField(blank=True,null=True,max_length=255)
    org_mail = models.EmailField(blank=True,null=True,max_length=255)
    org_fund = models.CharField(blank=True,null=True,max_length=255)

    def __str__(self):
        return self.organization_name

#ระดับชั้นการศึกษา ปริญญา สาขา เอก
class education_grade(models.Model):
    edu_grade = models.CharField(null=True,max_length=200)
    edu_degree = models.CharField(blank=True,default='NULL' ,max_length=200)
    edu_major = models.CharField(blank=True,null=True,max_length=200)

    def __str__(self):
        return self.edu_grade

#ชื่อมหาลัย ระดับชั้นการศึกษา
class education(models.Model):
    edu_id = models.AutoField(primary_key=True)
    edu_name = models.CharField(max_length=255)
    edu_grade = models.ForeignKey(education_grade,on_delete=models.CASCADE)

    def __str__(self):
        return self.edu_name

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
    sex_status = models.CharField(max_length=255, choices=sex)
    religion = models.ForeignKey(religions,blank=True,null=True,on_delete=models.CASCADE)
    status = models.CharField(max_length=100,choices=status_list)
    image = models.ImageField(blank=True,upload_to='images/')
    email = models.CharField(blank=True,null=True,max_length=255)
    mobiles = models.CharField(blank=True,null=True,max_length=20)  #ควรหาตัว validate เบอร์โทรใหม่และการสร้างใหม่เพราะ 1 คนสามารถมีได้หลายเบอร์
    dob = models.DateField(blank=True,null=True)
    addre = models.ForeignKey(address,blank=True,null=True,on_delete=models.CASCADE)
    latCo = models.CharField(blank=True,null=True,max_length=255)
    longCo = models.CharField(blank=True,null=True,max_length=255)
    relation = models.CharField(blank=True,null=True,max_length=255)
    friends = models.ManyToManyField("self",blank=True)
    # Srelation = models.CharField(max_length=255)
    #ประวัติการศึกษาควรทำอย่างไร
    edu_name = models.ForeignKey(education,blank=True,null=True,on_delete=models.CASCADE)
    # edu_grade = models.ForeignKey(education_grade,on_delete=models.CASCADE)
    # edu_degree = models.ForeignKey(education_grade,on_delete=models.CASCADE)
    # edu_major = models.ForeignKey(education_grade,on_delete=models.CASCADE)
    job = models.CharField(blank=True,null=True,max_length=255)
    organization_name = models.ForeignKey(organization,blank=True,null=True,on_delete=models.CASCADE)
    job_description = models.TextField(blank=True,null=True)
    facebook = models.CharField(blank=True,null=True,max_length=255)
    twitter = models.CharField(blank=True,null=True,max_length=255)
    instagram = models.CharField(blank=True,null=True,max_length=255)
    remark = models.TextField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = models.Manager()
    
    def __str__(self):
        return self.name

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
