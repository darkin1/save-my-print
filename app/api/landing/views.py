from django.shortcuts import render
from django.http import HttpResponse

def show(request):
    return HttpResponse("Hello, world. You're at the polls index.")
    
def form(request):
    return HttpResponse("This is form")