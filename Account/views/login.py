from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, HttpResponse
from django.views.generic import View
from django_mako_plus.controller import view_function
from .. import dmp_render, dmp_render_to_response
from django_mako_plus.controller.router import get_renderer
from django import forms
from django.contrib.auth import authenticate, login
from Account.models import User

@view_function
def process_request(request):

    if request.user.is_authenticated():
        return HttpResponseRedirect('/Account/index')

    form = login_form()
    if request.method == "POST":
        form = login_form(request.POST)
        if form.is_valid():
            login(request,form.user)
            return HttpResponse('''
            <script>
                window.location.reload();
            </script>
            ''')
    template_vars = {
        'form': form,
    }
    return dmp_render_to_response(request, 'login.html', template_vars)


class login_form(forms.Form):
    username = forms.CharField(label='username', required=True, max_length=30)
    password = forms.CharField(label='password', required=True, max_length=20 , widget=forms.PasswordInput())


    def clean(self):
        user = authenticate(username = self.cleaned_data.get('username'), password = self.cleaned_data.get('password'))
        if user == None:
            raise forms.ValidationError("This username and password are not correct.")
        self.user = user
        return self.cleaned_data
