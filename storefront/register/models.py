from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.utils.timezone import now
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import PermissionsMixin

from django.contrib.auth.password_validation import validate_password

import uuid
# Create your models here.


class CustomerManager(BaseUserManager):
    def create_user(self, email, date_of_birth, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, date_of_birth, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            date_of_birth=date_of_birth,
        )
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class Customer(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(
        unique=True,
        primary_key=True,
        default=uuid.uuid4)
    email = models.EmailField(unique=True)
    date_joined = models.DateTimeField(default=timezone.now)
    date_of_birth = models.DateField(null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['date_of_birth']

    objects = CustomerManager()

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):              # __unicode__ on Python 2
        return self.email


class HomePage(models.Model):
    """
    The settings for the homepage
    """
    page_title = models.CharField(max_length=200, null=False)
    logo_file = models.CharField(max_length=200, null=False)
    description = models.CharField(max_length=500)
    keywords = models.CharField(max_length=500)
    copyright_message = models.CharField(max_length=400, null=False)
    is_active = models.BooleanField(default=True)


class Slider(models.Model):
    """
    A slider model
    """
    name = models.CharField(max_length=200)
    is_active = models.BooleanField(null=False)
    images = models.ManyToManyField('Image')


class Image(models.Model):
    """
    An Image model to store all kind of images
    """
    image = models.ImageField(null=False)
    name = models.CharField(max_length=200)


class CustomerProfile(models.Model):
    """
    The customer profile's model
    """
    user = models.OneToOneField(Customer, on_delete=models.CASCADE)
    birthday = models.DateField(null=False)
    gender = models.CharField(null=False, max_length=10, default='Female')
    description = models.CharField(max_length=140)
    profile_picture = models.OneToOneField(Image, on_delete=models.CASCADE)
    created_date = models.DateField(default=now)
    phone_number = models.CharField(max_length=10)
    facebook_account = models.CharField(max_length=100)
    twitter_account = models.CharField(max_length=100)
    is_wholesaler = models.BooleanField(default=False)

# I think this model belongs to the store app


"""
class Address(models.Model):
    name = models.CharField()
    address_line_one = models.CharField(max_length=200)
    address_line_two = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    zip_number = models.CharField(max_length=10)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

"""
