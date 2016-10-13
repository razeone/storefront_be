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


class UserProfile(models.Model):
    """
    The user profile's model
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField('created date',
                                        default=now()
                                        )
    phone_number = models.CharField(max_length=10)
    is_wholesaler = models.BooleanField(default=False)
