#! /usr/bin/python3
# behrouz_ashraf
# garpozir@gmail.com
# -*- coding: utf-8 -*-

from django.urls import path,re_path
from .views import index, market

urlpatterns=[
    path('',index,name='index'),
    path('market/',market,name='market'),
    re_path(r'^market$',market,name='market'),
]
