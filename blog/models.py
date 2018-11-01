from django.db import models

# Create your models here.

# title
# pub_date
# body
# image

class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    objects = models.Manager()

    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[0:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')
        
# Add the blog app to the setting

# Create a migration

# Migrate

# Add the admin