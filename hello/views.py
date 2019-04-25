from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting
import redis

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')

    
    conn = redis.Redis(host='redis-10684.c1.asia-northeast1-1.gce.cloud.redislabs.com',port=10684,password='VUnd8roSLg2v5R9pX6apCsODHbwdSdVG')
    conn.set('k1','tttttt') # 向远程redis中写入了一个键值对
    return render(request, "index.html")


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})


