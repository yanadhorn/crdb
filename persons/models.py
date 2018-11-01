from django.db import models

# Create your models here.
# person class

class organization(models.Model):
    # org_id = models.AutoField(primary_key=True)
    organization_name = models.CharField(max_length=255)
    org_address = models.CharField(max_length=255)
    org_tel = models.CharField(max_length=255)
    org_field = models.CharField(max_length=255)
    org_mail = models.EmailField(max_length=255)
    org_fund = models.CharField(max_length=255)

class education_grade(models.Model):
    edugrade = (
        ('x','x1'),
        ('y', 'y1'),
        ('z', 'z1'),
    )
    edu_grade = models.CharField(max_length=200, choices = edugrade)


class education(models.Model):
    edu_id = models.AutoField(primary_key=True)
    edu_name = models.CharField(max_length=255)
    edu_grade = models.ForeignKey(education_grade,on_delete=models.CASCADE)

class Person(models.Model):
    person_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    summmary = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    email = models.CharField(max_length=255)
    status = models.CharField(max_length=100)
    dob = models.DateField()
    address = models.CharField(max_length=255)
    latCo = models.CharField(max_length=255)
    longCo = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    relation = models.CharField(max_length=255)
    Srelation = models.CharField(max_length=255)
    edu_id = models.ForeignKey(education,on_delete=models.CASCADE)
    job = models.CharField(max_length=255)
    organization_name = models.ForeignKey(organization,on_delete=models.CASCADE)
    facebook = models.CharField(max_length=255)
    twitter = models.CharField(max_length=255)
    instagram = models.CharField(max_length=255)
    remark = models.TextField()