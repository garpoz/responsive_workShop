#! /usr/bin/python3
# behrouz_ashraf
# garpozir@gmail.com
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.core.validators import MaxValueValidator,MinValueValidator
from django.conf import settings
from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver


class Hamkar(models.Model):
    SEMESTER_CHOICES = (
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
    )
    name = models.CharField(null=False, max_length=100, verbose_name="نام ")
    l_name = models.CharField(null=False, max_length=100, verbose_name="نام خانوادگی")
    market_name = models.CharField(
        null=False, max_length=100, verbose_name="نام فروشگاه"
    )
    city = models.CharField(null=False, max_length=100, verbose_name="نام شهر")
    user_name = models.CharField(unique=True, null=False, max_length=100, verbose_name="نام کاربری-انگلیسی وارد کنید")
    mobile_tel = models.BigIntegerField(
        validators=[MaxValueValidator(9999999999), MinValueValidator(1000000000)],
        null=False,
        unique=True,
        primary_key=True,
        verbose_name="شماره موبایل-گذرواژه",
    )
    market_tell = models.BigIntegerField(
        validators=[MaxValueValidator(9999999999), MinValueValidator(1000000000)],
        null=False,
        unique=True,
        verbose_name="تلفن ثابت با پیش شماره",
    )
    level = models.CharField(
        max_length=20, choices=SEMESTER_CHOICES, default="1", verbose_name="سطح دسترسی"
    )
    date_time = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ و ساعت ثبت")
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="چه کسی این کار را انجام می دهد",
    )

    def __str__(self):
        return "{} {}-{}-0{}".format(self.name, self.l_name, self.city, self.mobile_tel)


# @receiver(pre_delete, sender=market)
# def mymodel_delete(sender, instance, **kwargs):
#    instance.img.delete(False)
