#! /usr/bin/python3
# behrouz_ashraf
# garpozir@gmail.com
# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import Hamkar, Mahsool

admin.site.register(Hamkar)
admin.site.register(Mahsool)
