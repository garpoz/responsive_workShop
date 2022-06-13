#! /usr/bin/python3
# behrouz_ashraf
# garpozir@gmail.com
# -*- coding: utf-8 -*-

from django.urls import path,re_path
from .views import index

urlpatterns=[
    path('',index,name='index')
]
