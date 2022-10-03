from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import*
from .forms import*
from .serializers import*
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
import pandas as pd
import xlrd



# Create your views here.
@csrf_exempt
def mptnd_data(request):
    try:
        if request.method == "POST":
            data = MP_forms(request.POST, request.FILES)
            if data.is_valid():
                data.save()
                return JsonResponse({"status":"Successful","message": "File saved successfully"})
        return JsonResponse({"status":"Failed","message":"Invalid request method"})
    except Exception as e:
        return JsonResponse({"status":"Failed","message":f"Unknown error \n {e}"})



@csrf_exempt
def display_data(request):
    # try:
        if request.method == "GET":
            data_dict = {}
            show = MP_files.objects.all()
            show_serializer = MP_serializer(show, many = True)
            return JsonResponse(show_serializer.data, safe=False)
        if request.method == "POST":
            data1 = JSONParser().parse(request)  
            data1 = data1["file_name"]
            print(data1)                              
            dataframe = pd.read_excel(f"media/files/{data1}.xlsx")
            dataframe = dataframe.to_json(orient='records')            
            print(dataframe)
            return JsonResponse(dataframe, safe=False)
                # with open(f"media/{data}", errors="ignore") as f:
                #     print(f.read())
                    
                
                # data_list.append(dataframe1)
                # print(data_list)
            
        return JsonResponse({"status":"Failed","message":"Invalid request method"})
    # except Exception as e:
    #     return JsonResponse({"status":"Failed","message":f"Unknown error \n {e}"})












# @csrf_exempt
# def print_data(request):
#     if request.method == "POST":
#         data = JSONParser().parse(request)