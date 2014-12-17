import json
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods

@require_http_methods(["GET","POST"])
def home(request):
	text="Hello World"
	html="<html><body>%s</body></html>" % text
	rsp={}
	rsp['foo']='bar'
	return HttpResponse(json.dumps(rsp),content_type="application/json")

def all_restaurants(request):
	text="Restaurants"
	html= "<html><body>%s</body></html>" % text
	return HttpResponse(html)
