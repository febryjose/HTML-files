from django.db import models
from django.contrib.auth.models import User

class UserReg(models.Model):
    user = models.OneToOneField(User)
    address = models.CharField(max_length = 200)
    profileimage = models.ImageField(upload_to = 'uploaded_images', default='media/uploaded_images/default.jpeg')
    
    
    def __unicode__(self):
        return self.user.username
        
