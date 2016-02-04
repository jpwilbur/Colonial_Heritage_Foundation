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

    try:
        u = amod.User.objects.get(id=request.user.id)
    except amod.User.DoesNotExist:
        return HttpResponseRedirect('/Account/signup')
    form = edit_form()

    if request.method == "POST":
        form = edit_form(request.POST)
        form.userid = request.user.id
        if form.is_valid():
            u.set_password(form.cleaned_data.get('new_password1'))
            u.save()
            return HttpResponseRedirect('/homepage/index')
    template_vars = {
        'form': form,
    }
    return dmp_render_to_response(request, 'changepassword.html', template_vars)

class edit_form(forms.Form):
    username = forms.CharField(label='username', required=True, max_length=30)
    password = forms.CharField(label='password', required=True, max_length=20 , widget=forms.PasswordInput())
    new_password1 = forms.CharField(label='new_password1', required=True, max_length=20 , widget=forms.PasswordInput())
    new_password2 = forms.CharField(label='new_password2', required=True, max_length=20, widget=forms.PasswordInput())

    def clean(self):
        user = authenticate(username = self.cleaned_data.get('username'), password = self.cleaned_data.get('password'))
        if user == None:
            raise forms.ValidationError("This username and old password are not correct.")
        self.user = user
        return self.cleaned_data

        if self.cleaned_data.get('new_password1') != self.cleaned_data.get('new_password2'):
            raise forms.ValidationError('Passwords do not match. Try again.')
        return self.cleaned_data
