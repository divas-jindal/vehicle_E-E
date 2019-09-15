from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils.text import slugify
# from accounts.models import User

# pip install misaka
import misaka

from django.contrib.auth import get_user_model
User = get_user_model()

# https://docs.djangoproject.com/en/2.0/howto/custom-template-tags/#inclusion-tags
# This is for the in_group_members check template tag
from django import template
register = template.Library()


class fac(models.Model):
    name = models.CharField(max_length=255)
    vehicle_no = models.CharField(max_length=100, unique=True)
    vehicle_type = models.CharField(max_length=100)
    des = models.CharField(max_length=1000)

    def __str__(self):
        return self.vehicle_no
