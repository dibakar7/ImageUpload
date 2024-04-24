from django.db import models

# Create your models here.
class User_profile(models.Model):
    uploader_id = models.IntegerField()
    img = models.ImageField(upload_to='uploaded_img/', max_length=255, null=True, blank= False)
