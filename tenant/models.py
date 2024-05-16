from django.db import models

class SiteTenant (models.Model) : 
    name = models.SlugField(max_length=50,unique=True)
    user = models.ForeignKey('users.User',related_name='user_site',on_delete=models.CASCADE)
    about = models.TextField()
    is_working = models.BooleanField(default=True)
    jop_title = models.CharField(max_length=225)
