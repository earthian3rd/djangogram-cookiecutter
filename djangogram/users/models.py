from ast import BinOp
import email
from operator import mod
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    GENDER_CHOICE = [
        ('M', 'Male'),
        ('F', 'Femail'),
        ('C', 'Custom'),
    ]

    #: First and last name do not cover name patterns around the globe
    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    user_name = models.CharField(max_length=255, blank=True)
    profile_photo = models.ImageField(blank=True)
    website = models.URLField(max_length=255, blank=True)
    bio = models.TextField(blank=True)
    email  = models.CharField(max_length=255, blank=True)
    phone_number = models.CharField(max_length=255, blank=True)
    gender = models.CharField(max_length=255, blank=True, choices=GENDER_CHOICE)
    followers = models.ManyToManyField("self")
    following = models.ManyToManyField("self")
    
    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})
