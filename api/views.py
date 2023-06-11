from django.shortcuts import render
from .scrapper import Scrape
from django.conf import settings
from io import BytesIO
from django.http import JsonResponse, HttpResponse
from pathlib import Path
# 1. Import the csrf_exempt decorator
from django.views.decorators.csrf import csrf_exempt
import random
import json
# Create your views here.
def home(request):
 return HttpResponse('Hello there')
@csrf_exempt
def getResults(request):
    if(request.method=='POST'):
        links = json.loads(request.body).get('links')
        print(links)
        if(links):
            create_excel = Scrape()
            file_stream = BytesIO()
            create_excel(links, file_stream)
             # Serve the file for download
            file_stream.seek(0)
            response = HttpResponse(file_stream, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            response['Content-Disposition'] = 'attachment; filename="file.xlsx"'
            return response
    
    return JsonResponse({'success':False, 'msg': 'Bad Request'})
