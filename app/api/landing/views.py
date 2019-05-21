from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def show(request):
    return render(request, 'landing/show.html', context = {})

def privacy(request):
    return render(request, 'landing/privacy.html', context = {})

def terms(request):
    return render(request, 'landing/terms.html', context = {})

def assets(request):
    return render(request, 'landing/assets.html', context = {})

def form(request):
    return HttpResponse("This is form")