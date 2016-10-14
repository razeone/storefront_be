from django.db import models

from django.contrib.auth.models import User

from django.utils.timezone import now


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
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthday = models.DateField(null=False)
    description = models.CharField(max_length=140)
    profile_picture = models.OneToOneField(Image, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=now())
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
