from django.conf import settings
import os

def global_variables(request):
    return {
        'ENV': os.getenv('ENV'),
        'API_URL': os.getenv('API_URL'),
        'APP_URL': os.getenv('APP_URL'),
    }