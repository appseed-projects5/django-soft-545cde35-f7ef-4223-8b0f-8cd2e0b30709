# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    bio = models.CharField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Category(models.Model):

    #__Category_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)

    #__Category_FIELDS__END

    class Meta:
        verbose_name        = _("Category")
        verbose_name_plural = _("Category")


class Video(models.Model):

    #__Video_FIELDS__
    title = models.CharField(max_length=255, null=True, blank=True)

    #__Video_FIELDS__END

    class Meta:
        verbose_name        = _("Video")
        verbose_name_plural = _("Video")


class Req(models.Model):

    #__Req_FIELDS__
    uuid = models.CharField(max_length=255, null=True, blank=True)
    hwid = models.CharField(max_length=255, null=True, blank=True)
    username = models.CharField(max_length=255, null=True, blank=True)
    ip = models.CharField(max_length=255, null=True, blank=True)
    dvinf = models.CharField(max_length=255, null=True, blank=True)
    vid = models.CharField(max_length=255, null=True, blank=True)
    url = models.CharField(max_length=255, null=True, blank=True)

    #__Req_FIELDS__END

    class Meta:
        verbose_name        = _("Req")
        verbose_name_plural = _("Req")



#__MODELS__END
