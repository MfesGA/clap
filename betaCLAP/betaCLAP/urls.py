from django.conf.urls import patterns, include, url
from betaCLAP import views 

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
      url(r'^restaurants/', include('restaurants.urls')),
)
