#! /usr/bin/python3
# behrouz_ashraf
# garpozir@gmail.com
# -*- coding: utf-8 -*-

from django.shortcuts import render, HttpResponse, redirect
from .models import Hamkar
import socket, sqlite3
import requests
import os


def index(request):
    if request.GET:
        u_name = request.GET["user"]
        p_name = request.GET["pass"]
    return render(
        request,
        "colleague/index.html",
        {
            "headers": "+",
        },
    )
