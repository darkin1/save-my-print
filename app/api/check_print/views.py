from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import FileUploadSerializer

@api_view(['POST'])
def show(request):

   # from pudb.remote import set_trace; set_trace(term_size=(160, 40), host='0.0.0.0', port=6900)
   print('dupa')
   serializer = FileUploadSerializer(data=request.data)
   serializer.is_valid(raise_exception=True)
   file = request.FILES['file']

   # serializer.save()

   # print(request.data['aaa'])
   # print(request.FILES.get('file'))
   # print(request.POST.get('file'))

   # request.data

   return Response({
      'message': 'Success',
      'probability': '87',
      # 'aaa': request.data,
      'res': serializer.data,
   })