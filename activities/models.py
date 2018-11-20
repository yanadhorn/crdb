from django.db import models
from persons.models import person

# # Create your models here.
# class person_activites(models.Model):
#     act_status = (
#         ('Complete','เสร็จ'),
#         ('Pending','รอ'),
#         ('Progress','กำลังดำเนินการ'),
#         ('Start','เริ่ม')
#     )
#     image = models.ForeignKey(person,on_delete=models.DO_NOTHING)
#     relates_persons = models.ForeignKey(person,on_delete=models.DO_NOTHING)
#     relates_orgainzation = models.ForeignKey(person,on_delete=models.DO_NOTHING)
#     no_activites = models.CharField(max_length=255)
#     behavior = models.TextField(null=True)
#     activites_status = models.CharField(max_length=255,choices=act_status)

#     def __str__(self):
#         return self.behavior