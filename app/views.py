from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def msd(request):
    return HttpResponse('<h1> caption </h1>')