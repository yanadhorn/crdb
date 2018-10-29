from django.conf import settings
from django.db import models

def upload_update_image(instance,filename):
    return "update/{user}{filename}".format(user=instance.user, filename=filename)

# Create your models here.
class Update(models.Model):
    user        = models.ForeignKey(settings.Auth_USER_MODEL)
    content     = models.TextField()
    image       = models.ImageField(upload_to='upload_update_image', blank=True, null=True)
    updated     = models.DateTimeField(auto_now=True)
    timestamp   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content or ""    