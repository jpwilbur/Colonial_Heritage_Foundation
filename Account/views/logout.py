from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View
from django_mako_plus.controller import view_function
from .. import dmp_render, dmp_render_to_response
from django_mako_plus.controller.router import get_renderer
from django import forms
from django.contrib.auth import logout
from Account.models import User

@view_function
def process_request(request):
    logout(request)
    return HttpResponseRedirect('/homepage/index')
