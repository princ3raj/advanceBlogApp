from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect

from django.http import JsonResponse

from .models import Data

# Create your views here.


def index(request):
    return HttpResponse("Hi")


def api(request,phone_number,text_message):
    user=Data.objects.create(phone_number=phone_number,text_message=text_message)
    user.save()
    return HttpResponse("saved")

def fetchdata(request):
    datas=Data.objects.all()
    list=[]
    for data in datas:
        list.append(data.serialize())
    return JsonResponse(list, safe=False)
    

