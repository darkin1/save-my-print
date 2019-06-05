from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'check_print/show', views.show),
    url(r'check_print/image', views.image),
]