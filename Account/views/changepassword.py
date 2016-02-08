from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View
from django_mako_plus.controller import view_function
from .. import dmp_render, dmp_render_to_response
from django_mako_plus.controller.router import get_renderer
from django import forms
from django.contrib.auth import authenticate, login
import  Account.models as amod

@view_function
def process_request(request):

    #makes sure they are in the system to access this page. if not, redirected to sign up
    try:
        u = amod.User.objects.get(id=request.user.id)
    except amod.User.DoesNotExist:
        return HttpResponseRedirect('/Account/signup')
    form = edit_form()

    #if they hit submit button, this is true, otherwise goes over this and returns back to page with the empty form
    if request.method == "POST":
        form = edit_form(request.POST)
        #attaches username to form to be used in the clean data methods
        form.username = request.user.username
        if form.is_valid():
            u.set_password(form.cleaned_data.get('new_password1'))
            u.save()
            #doesnt work right now
            #u = authenticate(username = form.username, password = form.cleaned_data.get('password'))
            #u.login(request,form.user)
            return HttpResponseRedirect('/homepage/index')
    template_vars = {
        'form': form,
    }
    return dmp_render_to_response(request, 'changepassword.html', template_vars)

class edit_form(forms.Form):
    password = forms.CharField(label='Old Password', required=True, max_length=20 , widget=forms.PasswordInput())
    new_password1 = forms.CharField(label='New Password', required=True, max_length=20 , widget=forms.PasswordInput())
    new_password2 = forms.CharField(label='Comfirm New Password', required=True, max_length=20, widget=forms.PasswordInput())

    def clean(self):
        #uses that username attached to form and authenticates with the password they put in, the old password
        user = authenticate(username = self.username, password = self.cleaned_data.get('password'))
        if user == None:
            raise forms.ValidationError("This username and old password are not correct.")
            self.user = user
        elif self.cleaned_data.get('new_password1') != self.cleaned_data.get('new_password2'):
            raise forms.ValidationError('Passwords do not match. Try again.')
        return self.cleaned_data
