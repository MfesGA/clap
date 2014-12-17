from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from models import Minor_restaurant
from models import Loca_main
from models import *
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import ensure_csrf_cookie
import json
import datetime
from key_exchange import *

# Create your views here.

#view para adicionar o restaurante

@csrf_exempt
def addRSTR(request):
    context= RequestContext(request,{})
    data=json.loads(request.body)
    if request.method == 'POST':
        name = data.get('nameRestaurant')
        desc = data.get('descriptionRestaurant')
        chef = data.get('chefs')
        tcoz = data.get('cuisineType')
        lot  = data.get('capacityRestaurant')
        pre  = data.get('averagePrice')
        print(data.get('restaurantImage'))
        entry= Minor_restaurant(Rstr_name=name, Rstr_desc=desc, Rstr_chefs=chef, Rstr_tcoz=tcoz, Rstr_lot=lot )
        entry.save()
    return HttpResponse("Done")

#ver dados de todos os restaurantes
@ensure_csrf_cookie
def index(request):
    alt = Minor_restaurant.objects.order_by('-Rstr_name')
    rst = []
    for p in alt:
        rst.append(p.toJSON())
    return HttpResponse(json.dumps(rst),content_type="application/json")

#informacao especifica de um restaurante
@ensure_csrf_cookie
def indexfix(request, rest):
    field=rest.replace('_',' ')
    alt = Minor_restaurant.objects.filter(Rstr_name=field)
    print(alt)
    rst = []
    for p in alt:
        rst.append(p.toJSON())
    return HttpResponse(rst)


#menus
@csrf_exempt
def addmenu(request):
    context= RequestContext(request,{})
    data=json.loads(request.body)
    if request.method == 'POST':
        date=data.get('data')
        desc=data.get('desc')
        prec=data.get('preco')
        restn=data.get('rest')
        rest=Minor_restaurant.objects.filter(Rstr_name=restn)[0]
        res=Rstr_menu(Menu_date=date, Menu_desc=desc, Menu_rstr=rest, Menu_preco=prec)
        res.save()
    return HttpResponse("Done")
        
#adicionar um menu


#view de teste
@csrf_exempt
def rstrget(request):
    print(request)
    print("\n")
    if request.method == 'POST':
        print("post\n")
        print("forma do yoan:\n")
        print(json.loads(request.body))
    return HttpResponse("Done")

def parse_ct(ct):
    c = ct[:(len(ct)-16-1)]
    tag = ct[(len(ct)-16):]
    return (c,tag)

#vitor P^2 abaixo esta a tua view 
#login
@csrf_exempt
def logtrans(request):
    #podes printar o que vem do teu lado #print(request)
    #print("\n")
    #print(request)
    context= RequestContext(request,{})
    d=json.loads(request.body)    
    if request.method == 'POST':
        print(d)
        #manager = Restaurant.objects.filter(Rstr_mail=d)[0]
        #print(manager.Rstr_pass)
    return HttpResponse("Ready for key exchange")

@ensure_csrf_cookie
def locaget(request):
    alt = Loca_main.objects.all()
    loc = []
    for p in alt:
        loc.append( p.toJSON() )
    return HttpResponse(json.dumps(loc),content_type="application/json")

#@require_http_methods(["GET","POST"])

#Fabio work
@csrf_exempt
def locaput(request):
	#type(request)
	context= RequestContext(request,{})
	#print(request.body)
	d=json.loads(request.body)
	#print(context['lat'])
	print(d['lat'])
	print(d['lon'])
	print(d['type'])
	entry=Loca_main(Loca_desc=d['type'],Loca_lat=d['lat'],Loca_long=d['lon'])
	entry.save()
	return HttpResponse("Done")	
