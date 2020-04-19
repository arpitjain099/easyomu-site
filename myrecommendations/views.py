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
import urllib
from urllib.parse import urlparse
import urllib.parse
import requests
import time
import dns # required for connecting with SRV
import ssl

client = pymongo.MongoClient("mongodb://root:bA3xYORPcXHh" + '@35.197.160.225', ssl_cert_reqs=ssl.CERT_NONE)

db = client.easyomuwebsite
articledata = db.articles

def processLanguage(key):
    if key == "en":
        key = "translatedTextEn"
    elif key == "cn":
        key = "translatedTextChinese"
    elif key == "hi":
        key = "translatedTextHindi"
    elif key == "pa":
        key = "translatedTextPunjabi"
    elif key == "bn":
        key = "translatedTextBengali"
    elif key == "es":
        key = "translatedTextSpanish"
    elif key == "ae":
        key = "translatedTextArabic"
    elif key == "ms":
        key = "translatedTextMalay"
    elif key == "ru":
        key = "translatedTextRussian"
    elif key == "pt":
        key = "translatedTextPortuguese"
    elif key == "fr":
        key = "translatedTextFrench"
    elif key == "ja":
        key = "translatedTextJapanese"
    return key

def readMore(key):
    if key == "en":
        key = "Read More"
    elif key == "cn":
        key = "阅读更多"
    elif key == "hi":
        key = "अधिक पढ़ें"
    elif key == "pa":
        key = "ਹੋਰ ਪੜ੍ਹੋ"
    elif key == "bn":
        key = "আরও পড়ুন"
    elif key == "es":
        key = "Lee mas"
    elif key == "ae":
        key = "قراءة المزيد"
    elif key == "ms":
        key = "baca lebih lanjut"
    elif key == "ru":
        key = "Подробнее"
    elif key == "pt":
        key = "consulte Mais informação"
    elif key == "fr":
        key = "Lire la suite"
    elif key == "ja":
        key = "続きを読む"
    return key

def translation(key):
    if key == "en":
        key = "Translation"
    elif key == "cn":
        key = "翻译"
    elif key == "hi":
        key = "अनुवाद"
    elif key == "pa":
        key = "ਅਨੁਵਾਦ"
    elif key == "bn":
        key = "অনুবাদ"
    elif key == "es":
        key = "Traducción"
    elif key == "ae":
        key = "ترجمة"
    elif key == "ms":
        key = "terjemahan"
    elif key == "ru":
        key = "перевод"
    elif key == "pt":
        key = "tradução"
    elif key == "fr":
        key = "Traduction"
    elif key == "ja":
        key = "翻訳"
    return key


def details(request, country, language, topic):
    print(country)
    key = processLanguage(language)
    #searchOutput = articledata.find_one({'topic': topic, 'countryCode': country})
    tempSearchOutput = articledata.find({'category': topic, 'countryCode': country})
    print(topic)
    print(country)
    print(language)
    searchOutput = []
    for i in tempSearchOutput:
        searchOutput.append(i)
    searchOutput.sort(key=lambda x:x['publishedAt'])
    #print(searchOutput)
    outputList = []
    for newsArticleObject in reversed(searchOutput):
        #tempJson = {}
        #newsArticleObject[key] + "- " + newsArticleObject['contentPublisher'] + "<br>" + readMore(language) + newsArticleObject['url'] + "<br>" + translation(language) + "https://translate.google.com/translate?sl=auto&tl=" + language + "&u=" + urlparse(newsArticleObject(newsArticleObject['url']))
        outputJson = {}
        outputJson['imageurl'] = newsArticleObject['urlToImage']
        outputJson['title'] = newsArticleObject[key] + "- " + newsArticleObject['contentPublisher']
        outputJson['readmore'] = readMore(language)
        outputJson['translation'] = translation(language)
        outputJson['url'] = newsArticleObject['url']
        outputJson['translatedurl'] = "https://translate.google.com/translate?sl=auto&tl=" + language + "&u=" + urllib.parse.quote_plus(newsArticleObject['url'])
        #print(outputJson['url'])
        
        outputList.append(outputJson)
    outputList = {'output': outputList, 'language': language}
    return render(request, 'details.html', outputList)

def index(request):
    return render(request, 'index.html')