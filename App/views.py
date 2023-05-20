from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def Ajit(request):
    return HttpResponse("<marquee><b>He is a Batting Boy....</b></marquee>")