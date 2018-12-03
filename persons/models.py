from django.db import models

# Create your models here.
#ต้องใช้ autocomplete_fileds โดยจะต้องเพิ่ม table or class ใช้ 
class title_name(models.Model):
    title_short = models.CharField(blank=True,null=True,max_length=100)
    title_full = models.CharField(blank=True,null=True,max_length=100)

    def __str__(self):
        return self.title_short

#ศาสนา และนิกาย
class religions(models.Model):
    # person_id = models.ForeignKey(person,on_delete=models.CASCADE)
    religion = models.CharField(max_length=255)
    sect = models.CharField(blank=True,null=True,max_length=255)

    def __str__(self):
        return u'%s: %s'% (self.religion,self.sect)


class person(models.Model):
    sex = (
        ('male', 'ผู้ชาย'),
        ('female', 'ผู้หญิง'),
    )

    status_list = (
        ('single','โสด'),
        ('married','แต่งงาน'),
        ('divorce','หย่าร้าง'),
        ('complicated','ซับซ้อน'),
    )
    person_id = models.AutoField(primary_key=True)
    title_short = models.ForeignKey(title_name,blank=True,null=True,max_length=100,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    nickname = models.CharField(blank=True,null=True,max_length=100)
    sex_status = models.CharField(max_length=255, choices=sex)
    #เชื่อมไปยัง table religion
    religion = models.ForeignKey(religions,blank=True,null=True,on_delete=models.CASCADE)
    status = models.CharField(max_length=100,choices=status_list)
    image = models.ImageField(null=True,blank=True,upload_to='images/')
    email = models.EmailField(blank=True,null=True,max_length=255)
    dob = models.DateField(blank=True,null=True)
    # addre = models.ForeignKey(address,blank=True,null=True,on_delete=models.CASCADE)
    #ควรมี edu_profile หรือเปล่า
    # edu_name = models.ForeignKey(education,blank=True,null=True,on_delete=models.CASCADE)
    #ความสัมพันธ์อื่นๆ
    # relation = models.CharField(blank=True,null=True,max_length=255)
    friends = models.ManyToManyField("self",blank=True)
    familys = models.ManyToManyField("self",blank=True)
    #ตำแหน่งหน้าที่การงาน
    # jobs = models.ForeignKey(jobs,blank=True,null=True,on_delete=models.CASCADE)
    # personCoordinate = models.ForeignKey(personCoor,blank=True,null=True,on_delete=models.CASCADE)
    remark = models.TextField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = models.Manager()
    
    def __str__(self):
        return u'%s: %s '% (self.name,self.surname)

#ระดับชั้นการศึกษา ปริญญา สาขาเช่นคณะวิทยาศาสตร์ สาขาคอมพิวเตอรื
class education_grade(models.Model):
    edu_grade = models.CharField(null=True,max_length=200)
    edu_degree = models.CharField(blank=True,null=True,max_length=200)
    edu_major = models.CharField(blank=True,null=True,max_length=200)

    def __str__(self):
        return u'%s: %s %s'% (self.edu_grade,self.edu_degree,self.edu_major)
    # def __str__(self):
    #     return self.edu_grade

#ชื่อสถาบันการศึกษา ระดับชั้นการศึกษา ป.ตรี โท เอก
class education(models.Model):
    person_id = models.ForeignKey(person,blank=True,null=True,on_delete=models.CASCADE)
    edu_name = models.CharField(blank=True,null=True,max_length=255)
    edu_grade = models.ForeignKey(education_grade,on_delete=models.CASCADE)

    def __str__(self):
        return self.edu_name

class address(models.Model):
    person_id = models.ForeignKey(person,blank=True,null=True,on_delete=models.CASCADE)
    addre = models.CharField(blank=True,null=True,max_length=255)
    district = models.CharField(null=True,max_length=255)
    amphur = models.CharField(null=True,max_length=255)
    province = models.CharField(max_length=255)

    def __str__(self):
        return u'%s: %s %s %s'% (self.addre,self.district,self.amphur,self.province)

class jobs(models.Model):
    person_id = models.ForeignKey(person,blank=True,null=True,on_delete=models.CASCADE)
    job = models.CharField(blank=True,null=True,max_length=255)
    job_description = models.TextField(blank=True,null=True)

    def __str__(self):
        return str(self.job)

class personCoor(models.Model):
    person_id = models.ForeignKey(person,blank=True,null=True,on_delete=models.CASCADE)
    latitude = models.CharField(blank=True,null=True,max_length=255)
    longtitude = models.CharField(blank=True,null=True,max_length=255)

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

    def __str__(self):
        return self.contactType

# ประเภทขององค์กร รัฐ เอกชน สังคม
class org_categories(models.Model):
    org_categories = models.CharField(max_length=255)

    def __str__(self):
        return self.org_categories

class organization(models.Model):
    person_id = models.ForeignKey(person,blank=True,null=True,on_delete=models.CASCADE)
    organization_name = models.CharField(blank=True,null=True,max_length=255)
    org_address = models.CharField(max_length=255)
    org_categories = models.ForeignKey(org_categories,on_delete=models.CASCADE)
    org_website = models.URLField(blank=True,null=True)
    org_tel = models.CharField(blank=True,null=True,max_length=255)
    org_field = models.CharField(blank=True,null=True,max_length=255)
    org_mail = models.EmailField(blank=True,null=True,max_length=255)
    org_fund = models.CharField(blank=True,null=True,max_length=255)

    def __str__(self):
        return self.org_address

#บัญชี social media
class facebookAcc(models.Model):
    person_id = models.ForeignKey(person,blank=True,null=True,on_delete=models.CASCADE)
    facebook = models.URLField(blank=True,null=True,max_length=255)
    # facebook = models.ForeignKey(person,on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return self.facebook

class twitterAcc(models.Model):
    person_id = models.ForeignKey(person,blank=True,null=True,on_delete=models.CASCADE)
    twitter = models.URLField(blank=True,null=True,max_length=255)
    # twitter = models.ForeignKey(person,on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return self.twitter

class instagramAcc(models.Model):
    person_id = models.ForeignKey(person,blank=True,null=True,on_delete=models.CASCADE)
    instagram = models.URLField(blank=True,null=True,max_length=255)
    # instagram = models.ForeignKey(person,on_delete=models.CASCADE,blank=True,null=True)
    def __str__(self):
        return self.instagram

# class profiles(models.Model):
#     person_id = models.ForeignKey(person,blank=True,null=True,on_delete=models.CASCADE)
#     religion = models.ForeignKey(religions,blank=True,null=True,on_delete=models.CASCADE)
#     addre = models.ForeignKey(address,blank=True,null=True,on_delete=models.CASCADE)
#     contactType = models.ForeignKey(contact,blank=True,null=True,on_delete=models.CASCADE)
#     edu_name = models.ForeignKey(education,blank=True,null=True,on_delete=models.CASCADE)
#     organization_name = models.ForeignKey(organization,blank=True,null=True,on_delete=models.CASCADE)
#     job = models.ForeignKey(jobs,blank=True,null=True,on_delete=models.CASCADE)
#     personCoor = models.ForeignKey(personCoor,blank=True,null=True,on_delete=models.CASCADE)
#     facebook = models.ForeignKey(facebookAcc,blank=True,null=True,on_delete=models.CASCADE)
#     twitter = models.ForeignKey(twitterAcc,blank=True,null=True,on_delete=models.CASCADE)
#     instagram = models.ForeignKey(instagramAcc,blank=True,null=True,on_delete=models.CASCADE)


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
