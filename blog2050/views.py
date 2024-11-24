from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def blog2050_fun(request):

   if request.method == "GET":
       return HttpResponse("Loqta2050.com")
   elif request.method == "POST":
       return HttpResponse("This was a POST request")
    