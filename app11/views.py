from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def panth(request):
    return HttpResponse('<marquee><h1> best batsman in india now</h1><marquee>')