from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'landing/form', views.form),
    url(r'', views.show),
]