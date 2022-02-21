from django.db import models
from django.utils import timezone
from django.conf import settings

from django.conf import settings
from django.db.models.signals import post_save 
from django.dispatch import receiver 


from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionManager, PermissionsMixin)


class UserManager(BaseUserManager):
      def create_user(self, email, password=None, **extra_fields):

            if email is None:
                  raise TypeError('users should have an email')
            email = self.normalize_email(email)
            user = self.model(email=email,**extra_fields)
            user.set_password(password)
            user.save(using=self._db)
            return user

      def create_superuser(self, email, password, **extra_fields):
            extra_fields.setdefault('is_staff', True)
            extra_fields.setdefault('is_superuser', True)
            extra_fields.setdefault('is_active', True)
           
            extra_fields.setdefault('is_admin',True)
            if extra_fields.get('is_staff') is not True:
                  raise TypeError('superuser must be staff')
            return self.create_user(email, password, **extra_fields)

            # if password is None:
            #       raise TypeError('Password should not be None')
            # user = self.create_user(username, email, password)
            # user = self.model(username=username, email=self.normalize_email(email))
            # user.is_superuser = True
            # user.is_staff = True 
            # user.is_active = True
            # user.save(using=self._db)
            # return user 

class User(AbstractBaseUser, PermissionsMixin):

      first_name = models.CharField(max_length=40)
      last_name = models.CharField(max_length=40)
      organization = models.CharField(max_length=40)
      join_date = models.DateField(auto_now=True,auto_now_add=False)

      email = models.EmailField(max_length=255, unique=True, db_index=True)
      is_moderator=models.BooleanField(default=False)
      is_officer=models.BooleanField(default=False)
      is_admin=models.BooleanField(default=True)
      is_active=models.BooleanField(default=True)
      is_staff = models.BooleanField(default=False)
      added_by_user_id = models.IntegerField(default=0)

      address = models.CharField(max_length=500,default='',blank=True,null=True)
      profile_picture = models.ImageField(upload_to='profile_pictures/',default='profile_pictures/profile.jpg',blank=True,null=True)
      
      phone = models.CharField(max_length=22,null=True)
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at=models.DateTimeField(auto_now=True)

      objects = UserManager()

      USERNAME_FIELD = 'email'


      


      REQUIRED_FIELDS = ['organization','first_name']
