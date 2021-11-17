from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.related import OneToOneField
from django.dispatch import receiver
from django.db.models.signals import post_save

class Profile(models.Model):
    user = models.OneToOneField(User, null=False, on_delete=models.CASCADE, primary_key=True)
    actif = models.BooleanField(default=True)
    photo = models.ImageField(null=True, blank=True, upload_to='documents/')
    phone = models.CharField(blank=True, max_length=15, null=True)
    birth_date = models.DateField(null=True, blank=True)
    country = models.CharField(blank=True, max_length=100, null=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    is_admin = models.BooleanField(default=False)


    def __str__(self):
        return '%s %s' % (self.user.first_name, self.user.last_name)
    
    @receiver(post_save, sender=User)
    def update_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
        instance.profile.save()
    
class Post(models.Model):
    idpo = models.CharField(max_length=1000, primary_key=True)
    message = models.TextField(max_length=4000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    photo = models.ImageField(null=True, blank=True, upload_to='documents/')
    created_by = models.ForeignKey(Profile, null=True, related_name='posts', on_delete=models.SET_NULL)

class Pet(models.Model):
    idp = models.CharField(max_length=1000,primary_key=True)
    pet = models.TextField(max_length=40)
    birth_date = models.DateTimeField(null=True)
    photo = models.ImageField(null=True, blank=True, upload_to='documents/')
    height = models.TextField(max_length=40)
    weight = models.TextField(max_length=40)
    pet_type = models.TextField(max_length=40)
    medical_condition = models.TextField(max_length=4000)
    pet_owner = models.ForeignKey(Profile, null=True, related_name='pet', on_delete=models.SET_NULL)
    #location = models.PointField()
