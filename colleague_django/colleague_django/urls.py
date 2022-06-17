#! /usr/bin/python3
# behrouz_ashraf
# garpozir@gmail.com
# -*- coding: utf-8 -*-

from django.contrib import admin
from django.urls import path, include,re_path
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_title = 'پنل مدیریت'
admin.site.site_header = 'به نام خدا'
admin.site.index_title = 'بخش مدیریت کاربران و محصولات'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('colleague.urls')),
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

