from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View
from django_mako_plus.controller import view_function
from .. import dmp_render, dmp_render_to_response
from django_mako_plus.controller.router import get_renderer

templater = get_renderer('homepage')

@view_function
def process_request(request):
    params = {}
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        print (name,email)
        return HttpResponseRedirect("/homepage/index")
    return templater.render_to_response(request, "contact.html", params)
