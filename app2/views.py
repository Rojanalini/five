from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def India(request):
    return HttpResponse('<h1> won the match </h1>')