from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'landing/form', views.form),
    url(r'privacy', views.privacy),
    url(r'terms', views.terms),
    url(r'assets', views.assets),
    url(r'', views.show),
]