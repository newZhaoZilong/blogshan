from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# from django.views.decorators.csrf import requires_csrf_token
# Create your views here.
import json


@csrf_exempt
def getbloginfo(request):
    print('有没有走到这一步')
    name_dict = {
        'name':'shangeblog',
        'desc':'测试返回json'
    }

    return HttpResponse(json.dumps(name_dict),content_type='application/json')