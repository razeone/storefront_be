from django.db import models

from django.contrib.auth.models import User

from django.utils.timezone import now


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField('created date',
                                        default=now()
                                        )
    phone_number = models.CharField(max_length=10)
    is_wholesaler = models.BooleanField(default=False)
