from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View
from django_mako_plus.controller import view_function
from .. import dmp_render, dmp_render_to_response
from django_mako_plus.controller.router import get_renderer
from django import forms
import  Account.models as amod

@view_function
def process_request(request):
     users = amod.User.objects.all().order_by('last_name','first_name')

     template_vars = {
         'users': users,
     }
     return dmp_render_to_response(request, 'users.html', template_vars)
