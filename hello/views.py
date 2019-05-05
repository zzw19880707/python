from django.shortcuts import render
from django.http import HttpResponse
import requests
from .models import Greeting
import redis
import pymongo 

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')

    # pool = redis.ConnectionPool(host='localhoredis-10684.c1.asia-northeast1-1.gce.cloud.redislabs.comst', port=10684,password='VUnd8roSLg2v5R9pX6apCsODHbwdSdVG', decode_responses=True)  
    # r = redis.Redis(connection_pool=pool)
    # r.set('k1','tttttt') # 向远程redis中写入了一个键值对
    # client = pymongo.MongoClient("mongodb+srv://zzw19880707:shazi31@cluster0-1ogxa.azure.mongodb.net/test?retryWrites=true")
    # db = client.test
    # return render(request, "index.html")
    r = requests.get('http://httpbin.org/status/418')
    print(r.text)
    return HttpResponse('<pre>' + r.text + '</pre>')

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})


