from django.conf import settings
from django_hosts import patterns, host

host_patterns = patterns('',
    # host(r'app', 'api.urls', name='api'),
    host(r'admin', settings.ROOT_URLCONF, name='admin'),
    host(r'api', 'api.urls_api', name='api'),
    host(r'www', 'api.urls_www', name='www'),
)