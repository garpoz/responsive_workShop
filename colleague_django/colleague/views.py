#! /usr/bin/python3
# behrouz_ashraf
# garpozir@gmail.com
# -*- coding: utf-8 -*-

from colleague_django.settings import BASE_DIR
from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponseRedirect
from .models import Hamkar, Mahsool
import socket, sqlite3
import requests
import os
from django.db.models import Max,Q


def index(request):
    return render(
        request,
        "colleague/index.html",
    )

def market(request):
    if request.GET:
        u_name = request.GET["user"]
        p_name = request.GET["pass"]
        p_name=''.join(list(map(lambda z:chr(int(z)),p_name.split('👌')[1:])))
        if p_name.isdigit()==False:
            return redirect('/')
        qury=Hamkar.objects.filter(
            Q(user_name=u_name) & Q(mobile_tel=p_name[1:])
        )
        if qury.count()==0:
            return redirect('/')
        else:
            f_name=qury[0].name+' '+qury[0].l_name
            you_level=qury[0].level
            conn = sqlite3.connect(f"{BASE_DIR}/db.sqlite3")
            cur = conn.cursor()
            cur.execute(f"select name,num_pack,num_box,invent,date_time,url,mony{you_level} from colleague_mahsool;")
            headers = cur.fetchall()
            conn.close()
            lst=[]
            for m in headers:
                amo=m[6]
                txt = '{pr:,}'
                amo=txt.format(pr=amo)
                lst.append(m)
                #lst.append(amo)
            return render(
                request,
                "colleague/market.html",
                {'headers':headers,
                 'amo':lst,
                'f_name':f_name
                })
    else:
        return redirect('/')
