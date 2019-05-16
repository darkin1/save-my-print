from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def show(request):
    return render(request, 'landing/show.html', context = {})
    
def form(request):
    return HttpResponse("This is form")