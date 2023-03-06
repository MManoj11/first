from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def sample(request):
    return HttpResponse('<h1>welcome to django project</h1>')

def sample1(request):
    return HttpResponse('<marquee><h1> project is successfully executed </h1><marquee>')
