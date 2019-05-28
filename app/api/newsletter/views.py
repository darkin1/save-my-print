from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import NewsletterSerializer
from mailchimp3 import MailChimp

@api_view(['GET', 'POST'])
def save(request):

    serializer = NewsletterSerializer(data=request.data)
    try:
        serializer.is_valid(raise_exception=True)
    except:
        return Response({
            'message': "Email may not be blank"
        }, 412)

    client = MailChimp(mc_api='14f15a6cf85d6511cb67ac3eb2270e36-us20', mc_user='Dariusz Ciesielski')
    # lists = client.lists.all()
    # lists = client.lists.get('6f9421b0ae')

    try:
        c = client.lists.members.get('6f9421b0ae', request.data['email'])
    except:
        client.lists.members.create('6f9421b0ae', {
            'email_address': request.data['email'],
            'status': 'subscribed',
            # 'merge_fields': {
                # 'FNAME': 'John',
                # 'LNAME': 'Doe',
            # },
        })

        return Response({
            "message": 'Thanks for subscribing. You will be the first to known about new releases and updates. Stay tuned.' ,
        })

    return Response({
        'message': 'The email already exists',
    }, 400)