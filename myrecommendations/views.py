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

def details(request, restaurantId, language):
    searchOutput = menudata.find_one({'restaurantId': restaurantId })
    outputJson = {}
    if searchOutput == None:
        print("not found")
        return render(request, 'details.html', outputJson)
    else:
        print("found")
        sectionArray = []
        #print(searchOutput)
        #print("testing")
        for section in searchOutput['sections']:
            dishArray = []
            #print(section)
            for dishObject in section['dishes']:
                #print(dishObject)
                if language in dishObject['title'].keys():
                    dish = {}
                    dish['title'] = dishObject['title'][language]
                    dish['description'] = dishObject['description'][language]
                    dish['imageUrl'] = dishObject['imageUrl']
                    dish['priceWithoutTax'] = dishObject['priceWithoutTax']
                    dish['priceWithTax'] = dishObject['priceWithTax']
                    dishArray.append(dish)
            jsonObject = {}
            jsonObject['sectionName'] = section['name'][language]
            jsonObject['dishes'] = dishArray
            sectionArray.append(jsonObject)
        #print(sectionArray)
        outputJson = {'output': sectionArray, 'language': language}
        print(outputJson)
        return render(request, 'details.html', outputJson)