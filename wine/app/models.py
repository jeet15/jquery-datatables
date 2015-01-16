from django.db import models
from wine.settings import PHOTO_UPLOAD_DIR

# Create your models here.

class Car(models.Model):
    name = models.CharField(max_length=120)
    image = models.FileField(upload_to = PHOTO_UPLOAD_DIR)

    def __unicode__(self):
        return self.name

    def image_info(self):
        url = "No attachment"
        if self.image:
            url = self.image.url.split('/',5)
            if len(url) > 1:
                url = '/' + url[5]
            else:
                url = "No attachment"
        return url    

class User(models.Model):
    name = models.CharField(max_length=120)
    email = models.CharField("Email", max_length=32)
    username = models.CharField(max_length = 32)