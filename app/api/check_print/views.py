from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import FileUploadSerializer
from django.core.files.storage import FileSystemStorage

@api_view(['POST'])
def show(request):

   # from pudb.remote import set_trace; set_trace(term_size=(160, 40), host='0.0.0.0', port=6900)

   serializer = FileUploadSerializer(data=request.data)
   serializer.is_valid(raise_exception=True)
   file = request.FILES['file']

   # TODO: save information about probalitity to database?

   fs = FileSystemStorage(location='./../static/uploaded', file_permissions_mode=775)
   filename = fs.save(file.name, file)
   uploaded_file_url = fs.url(filename)

   return Response({
      'message': 'Success',
      'probability': '87',
      # 'aaa': request.data,
      'res': serializer.data,
      'uploaded_file_url': uploaded_file_url
   })