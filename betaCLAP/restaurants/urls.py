from django.conf.urls import patterns, include, url
from restaurants import views 

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('restaurants.views',
    # Examples:
   url(r'^main/','index',name='index' ),#todos os restaurantes
   url(r'^spec/([a-z A-Z _]*)','indexfix',name='indexfix' ), #um restaurante em especifico
   url(r'^menu/view','menu'   ,name='menu' ),#ver o menu
   url(r'^menu/add' ,'addmenu',name='addmenu'),#adicionar um menu
   url(r'^teste/','rstrget',name='locaget' ), # rstrgat  ir ver ao views.py 
   url(r'^input/','addRSTR',name='addRSTR' ),
   url(r'^main/input/','rstrget',name='rstrget' ),# To Fabio 

   url(r'^local/get/','locaget',name='rstrgets' ),
   url(r'^local/put/','locaput',name='rstrgets'),
   url(r'^login/','logtrans',name='rstrgets' ),

   #url(r'^auth/','crp',name='' ),
)
