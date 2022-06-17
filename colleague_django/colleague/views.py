#! /usr/bin/python3
# behrouz_ashraf
# garpozir@gmail.com
# -*- coding: utf-8 -*-

from django.shortcuts import render, HttpResponse, redirect
from .models import Hamkar
import socket, sqlite3
import requests
import os
from django.db.models import Max,Q


def index(request):
    if request.GET:
        u_name = request.GET["user"]
        p_name = request.GET["pass"]
        if p_name.isdigit()==False:
            return redirect('/')
        qury=Hamkar.objects.filter(
            Q(user_name=u_name) & Q(mobile_tel=p_name[1:])
        )
        if qury.count()==0:
            return redirect('/')
        else:
            return redirect(f'/market?ok={u_name}')
    else:
        return render(
            request,
            "colleague/index.html",
        )
