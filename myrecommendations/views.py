from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.generic import UpdateView
from django.utils import timezone


import os
import json
import codecs
import pymongo
from pymongo import MongoClient
import urllib.parse
import requests
import time
import dns # required for connecting with SRV
import ssl

client = pymongo.MongoClient("mongodb+srv://arpitjain099:Xerox123@cluster0-gstg9.gcp.mongodb.net", ssl_cert_reqs=ssl.CERT_NONE)

db = client.easyeat
menudata = db.menu


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def details(request):
    searchOutput = menudata.find({})
    for i in searchOutput:
        context = {'searchOutput': i, 'language': 'en'}
        for i in searchOutput:
            print(i)
        print(context)
        return render(request, 'details.html', context)