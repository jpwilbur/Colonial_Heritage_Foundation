from .. import dmp_render, dmp_render_to_response
from django.template import RequestContext
import json
import catalog.models as cmod
from Account import models as amod
from django.conf import settings
from django import forms
from django.forms.models import model_to_dict
from django.http import HttpResponse, HttpResponseRedirect
from django_mako_plus.controller import view_function
from .. import dmp_render, dmp_render_to_response

@view_function
def process_request(request):
	if request.is_ajax():
		try:
			q = cmod.Product.objects.get(id=request.urlparams[0])
		except cmod.Product.DoesNotExist:
			return HttpResponseRedirect('/catalog/products')
		qtyData = q.quantityAvailable
		data = json.dumps(qtyData)
		return HttpResponse(data, content_type='application/json')
	else:
		raise Http404
		print('Didnt work')
