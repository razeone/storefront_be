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
    use_in_migrations = True

    def _create_customer(
            self,
            email,
            password,
            is_staff,
            is_superuser,
            **extra_fields):
        now = timezone.now()
        if not email:
            raise ValueError('The given email must be set')
        if not password:
            raise ValueError('The given password must be set')
        email = self.normalize_email(email)
        customer = self.model(email=email, is_staff=is_staff,
                              is_superuser=is_superuser, is_active=True,
                              date_joined=now, **extra_fields)

        validate_password(password)
        customer.set_password(password)
        customer.save(using=self._db)
        return customer

        def create_user(self, email, password=None, **extra_fields):
            return self._create_customer(
                email,
                password,
                False,
                False,
                **extra_fields)

        def create_superuser(self, email, password, **extra_fields):
            return self._create_customer(
                email,
                password,
                True,
                True,
                **extra_fields)


class Customer(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(
        unique=True,
        primary_key=True,
        default=uuid.uuid4)
    email = models.EmailField(unique=True)
    date_joined = models.DateTimeField(default=timezone.now)
    date_of_birth = models.DateField(null=True)
    is_staff = models.BooleanField(
        default=False,
        help_text='Designates whether the customer can log into this admin.')
    is_active = models.BooleanField(
        default=False,
        help_text='Designates whether this customer should be treated as active.')

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
