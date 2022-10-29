import json
from django.shortcuts import render
from core.models import *
from django.db.models import Q
from django.http import JsonResponse
# Create your views here.

def get_words(request):
    if request.method == 'GET' and 'search_key' in request.GET:
        query = request.GET['search_key'] 
        res_words = list(words.objects.filter(
            Q(word__icontains=query) | 
            Q(pronunciation__icontains=query) |  
            Q(meaning__icontains=query) | 
            Q(desc__icontains=query)
        ).values_list())
        return JsonResponse(json.dumps({
            'status_code' : 200,
            'status' : 'success',
            'msg' : 'data',
            'data' : res_words
        }), safe=False)
    return JsonResponse(json.dumps({
        'status_code' : 400,
        'status' : 'error',
        'msg' : '`search_key` is not defined'
    }), safe=False)