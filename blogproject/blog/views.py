from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


from django.http import JsonResponse

from django.views.decorators.http import require_http_methods
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt




@require_http_methods(['GET'])
def getIndex(request):
    response = "You're looking at the results of question %s."
    return render(request,'index.html')
    # return render(request,'index.html')

@require_http_methods(['GET'])
def testGET(request):

    return JsonResponse({'msg':'GET'})


# @csrf_exempt装饰器能避免'django.middleware.csrf.CsrfViewMiddleware'的检测
@csrf_exempt
@require_http_methods(['POST'])
def testPOST(request):

    return JsonResponse({'msg':'POST'})


