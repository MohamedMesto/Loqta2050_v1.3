from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home_func(request):

   if request.method == "GET":
       return HttpResponse("Welcome to Un2050.de")
   elif request.method == "POST":
       return HttpResponse("This was a POST request")
    