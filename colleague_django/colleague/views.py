#! /usr/bin/python3
# behrouz_ashraf
# garpozir@gmail.com
# -*- coding: utf-8 -*-

from django.shortcuts import render, HttpResponse,redirect
import socket,sqlite3
import requests
import os

def index(request):
    return render(request,'colleague/index.html',{'headers':'+',
                })
