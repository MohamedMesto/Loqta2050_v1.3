from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.


def aboutus_func(request):
   if request.method == "GET":
       return HttpResponse("Welcome to our world of innovation, where creativity meets technology. With over 15 years of experience, our team of skilled full-stack developers and a visionary graphic designer brings your ideas to life. We specialize in crafting cutting-edge web and mobile applications, paired with stunning graphic designs. Our solutions are tailored to elevate your brand and drive success. From concept to completion, we deliver excellence with every project. Let's build something extraordinary together!")
   elif request.method == "POST":
       return HttpResponse("This was an aboutus POST request")
    