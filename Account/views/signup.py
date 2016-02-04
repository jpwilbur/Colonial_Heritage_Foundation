from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View
from django_mako_plus.controller import view_function
from .. import dmp_render, dmp_render_to_response
from django_mako_plus.controller.router import get_renderer
from django import forms
from Account.models import User

@view_function
def process_request(request):
    form = signup_form()
    if request.method == "POST":
        form = signup_form(request.POST)
        if form.is_valid():
            u = User()
            u.username = form.cleaned_data.get('username')
            u.first_name = form.cleaned_data.get('first_name')
            u.last_name = form.cleaned_data.get('last_name')
            u.email = form.cleaned_data.get('email')
            u.address1 = form.cleaned_data.get('address1')
            u.address2 = form.cleaned_data.get('address2')
            u.birth = form.cleaned_data.get('birth')
            u.phone_number = form.cleaned_data.get('phone_number')
            u.set_password(form.cleaned_data.get('password'))
            u.save()
            return HttpResponseRedirect('/homepage/index')
    template_vars = {
        'form': form,
    }
    return dmp_render_to_response(request, 'signup.html', template_vars)


class signup_form(forms.Form):
    username = forms.CharField(label='username', required=True, max_length=30)
    first_name = forms.CharField(label='first_name', required=True, max_length=30)
    last_name = forms.CharField(label='last_name', required=True, max_length=30)
    email = forms.EmailField(label='email', required=True)
    address1 = forms.CharField(label='address1', required=True, max_length=30)
    address2 = forms.CharField(label='address2', required=True, max_length=30)
    birth = forms.DateField(label='birth', required=True)
    phone_number = forms.CharField(label='phone_number', required=True, max_length=20)
    password = forms.CharField(label='password', required=True, max_length=20 , widget=forms.PasswordInput())
    password2 = forms.CharField(label='password2', required=True, max_length=20, widget=forms.PasswordInput())

    def clean_username (self):
        if User.objects.filter(username=self.cleaned_data.get('username')).count() > 0:
            raise forms.ValidationError('That username already exists in our system.')
        return self.cleaned_data['username']

    def clean(self):
        if self.cleaned_data.get('password') != self.cleaned_data.get('password2'):
            raise forms.ValidationError('Passwords do not match. Try again.')
        return self.cleaned_data
