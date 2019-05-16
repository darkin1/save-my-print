from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['POST', 'GET'])
def show(request):
   return Response({'message': 'show'})