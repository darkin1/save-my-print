from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'newsletter/save', views.save),
]