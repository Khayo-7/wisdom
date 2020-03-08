from django.db import models

# # Create your models here.
# from django.contrib.auth.models import AbstractBaseUser
# from django.contrib.auth.models import PermissionsMixin
# from django.contrib.auth.models import BaseUserManager
# # Create your models here.

# """User manager class"""

# class UserProfileManager(BaseUserManager):
    
#     def create_user(self, email, first_name, middle_name, last_name, password = None):
#         if not email:
#             raise ValueError("Email Address is required")
#         email = self.normalize_email(email)
#         user = self.model(email = email, first_name = first_name, middle_name = middle_name, last_name = last_name)
#         user.set_password(password)
#         user.save(using=self._db)

#         return user

#     def create_superuser(self, email, first_name, middle_name, last_name, password):

#         user = self.create_user(email, first_name, middle_name, last_name, password)
#         user.is_superuser = True
#         user.is_staff = True
#         user.status = 'Super Admin'
#         user.save(using=self._db)

#         return user

# """User profile"""
# class UserProfile(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(max_length = 255, unique = True)
#     first_name = models.CharField(max_length=255)
#     middle_name = models.CharField(max_length=255)
#     last_name = models.CharField(max_length=255)
#     status = models.CharField(max_length=25)
#     is_staff = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=False)

#     objects = UserProfileManager()
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['first_name', 'email']

#     def get_full_name(self):
#         return self.first_name + self.middle_name + self.last_name

#     def get_short_name(self):
#         return self.first_name 

#     def get_email(self):
#         return self.email

#     def __str__(self):
#         return self.email
