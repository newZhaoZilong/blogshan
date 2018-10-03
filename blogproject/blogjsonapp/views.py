from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import json

def getbloginfo(request):
    name_dict = {
        'name':'shangeblog',
        'desc':'测试返回json'
    }

    return HttpResponse(json.dumps(name_dict),content_type='application/json',)