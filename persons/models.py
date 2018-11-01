from django.db import models

# Create your models here.
# person class
class org_categories(models.Model):
    org_categories = models.CharField(max_length=255)

class organization(models.Model):
    # org_id = models.AutoField(primary_key=True)
    organization_name = models.CharField(max_length=255)
    org_address = models.CharField(max_length=255)
    org_categories = models.ForeignKey(org_categories,on_delete=models.CASCADE)
    org_tel = models.CharField(max_length=255)
    org_field = models.CharField(max_length=255)
    org_mail = models.EmailField(max_length=255)
    org_fund = models.CharField(max_length=255)

class education_grade(models.Model):
    edu_grade = models.CharField(max_length=200)
    edu_degree = models.CharField(default='NULL' ,max_length=200)
    edu_major = models.CharField(max_length=200)

class education(models.Model):
    edu_id = models.AutoField(primary_key=True)
    edu_name = models.CharField(max_length=255)
    edu_grade = models.ForeignKey(education_grade,on_delete=models.CASCADE)

class religion(models.Model):
    religion = models.CharField(max_length=255)
    sect = models.CharField(max_length=255)

class Person(models.Model):
    sex = (
        ('male', 'ผู้ชาย'),
        ('female', 'ผู้หญิง'),
    )
    person_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    sex_status = models.CharField(max_length=255, choices=sex)
    religion = models.ForeignKey(religion,on_delete=models.CASCADE)
    status = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    email = models.CharField(max_length=255)
    mobiles = models.CharField(max_length=20)  #ควรหาตัว validate เบอร์โทรใหม่และการสร้างใหม่เพราะ 1 คนสามารถมีได้หลายเบอร์
    dob = models.DateField()
    address = models.CharField(max_length=255)
    latCo = models.CharField(max_length=255)
    longCo = models.CharField(max_length=255)
    relation = models.CharField(max_length=255)
    Srelation = models.CharField(max_length=255)
    #ประวัติการศึกษาควรทำอย่างไร
    edu_name = models.ForeignKey(education,on_delete=models.CASCADE)
    # edu_grade = models.ForeignKey(education_grade,on_delete=models.CASCADE)
    # edu_degree = models.ForeignKey(education_grade,on_delete=models.CASCADE)
    # edu_major = models.ForeignKey(education_grade,on_delete=models.CASCADE)
    job = models.CharField(max_length=255)
    organization_name = models.ForeignKey(organization,on_delete=models.CASCADE)
    job_description = models.TextField()
    facebook = models.CharField(max_length=255)
    twitter = models.CharField(max_length=255)
    instagram = models.CharField(max_length=255)
    remark = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)