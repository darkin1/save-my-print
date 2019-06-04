from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import FileUploadSerializer
from django.core.files.storage import FileSystemStorage
import skimage
from skimage.transform import resize
import os
import numpy as np
import json
import requests


@api_view(['GET'])
def image(request):
   IMG_SIZE = 160
   path = './../static/dataset_test'
   ## FAILED
   # img = '0004.jpg'
   # img = 'B0tLsXHCYAAAeq-.jpg'
   # img = 'DwX7Vz9uVgdx_HqV0-gefJ4FI8btsuB3BmmtrgCIvi4.jpg'
   # img = 'fsc.jpg'
   # img = 'hqdefault.jpg'
   # img = 'mess2_sm.jpg'
   # img = 'musical_mouthpiece_attempt1-600.jpg'

   ## GOOD
   path = './../static/dataset_test/good'
   # img = '5e04faf6b1ebee0735ffb82771ca9051_preview_featured.jpg'
   # img = 'BV-Acharya-9.jpg'
   # img = 'fused-filament-fabrication-fff-thumb-600x300.jpg'
   # img = 'images.jpg'
   # img = 'index.jpg'


   image = skimage.io.imread(os.path.join(path, img))
   image = resize(image, (IMG_SIZE, IMG_SIZE))

   # If grayscale. Convert to RGB for consistency.
   if image.ndim != 3:
       image = skimage.color.gray2rgb(image)

   data = json.dumps({"signature_name": "serving_default", "instances": [image.tolist()]})

   headers = {"content-type": "application/json"}
   json_response = requests.post('http://tensorflow-serving:8501/v1/models/half_plus_two:predict', data=data, headers=headers)
   predictions = json.loads(json_response.text)['predictions']

   return Response({
       'message': 'ok',
       'prediction': predictions
   })


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
