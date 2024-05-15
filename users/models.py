from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify


class user_objects (BaseUserManager) :
    def create_user (self,email,password,**fields) : 
        email = self.normalize_email(email)
        user = self.model(**fields)
        user.email = email
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self,**fields) : 
        fields['is_staff'] = True
        fields['is_superuser'] = True
        return self.create_user(**fields)
    

class User (AbstractUser) : 
    objects = user_objects()

    username = None
    first_name = None
    last_name = None

    full_name = models.CharField(max_length=225)
    email = models.EmailField(unique=True)
    picture = models.ImageField(upload_to='user-pics/',default='user.png')
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('full_name',)

    def __str__(self) -> str:
        return self.full_name
    
class Site (models.Model) : 
    name = models.SlugField(max_length=50,unique=True)
    user = models.ForeignKey(User,related_name='user_site',on_delete=models.CASCADE)
    about = models.TextField()
    is_working = models.BooleanField(default=True)
    jop_title = models.CharField(max_length=225)

@receiver(post_save,sender=User)
def create_site_for_user(created, instance:User,**kwargs) : 
    if created:
        site = Site(user=instance,name=slugify(instance.full_name))
        site.save()