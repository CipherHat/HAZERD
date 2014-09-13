__author__ = 'cipherhat'

from django.conf.urls import url
from visa_sponsor import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^result/', views.parseHTML, name="parseHTML")
    ]