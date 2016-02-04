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

    template_vars = {}

    try:
        u = amod.User.objects.get(id=request.user.id)
    except amod.User.DoesNotExist:
        return HttpResponseRedirect('/Account/signup')

    form = edit_form( initial = {
        'username' : u.username,
        'first_name' : u.first_name,
        'last_name' : u.last_name,
        'email' : u.email,
        'address1' : u.address1,
        'address2' : u.address2,
        'birth' : u.birth,
        'phone_number' : u.phone_number,
    })

    if request.method == "POST":
        form = edit_form(request.POST)
        form.userid = request.user.id
        if form.is_valid():
            u.username = form.cleaned_data.get('username')
            u.first_name = form.cleaned_data.get('first_name')
            u.last_name = form.cleaned_data.get('last_name')
            u.email = form.cleaned_data.get('email')
            u.address1 = form.cleaned_data.get('address1')
            u.address2 = form.cleaned_data.get('address2')
            u.birth = form.cleaned_data.get('birth')
            u.phone_number = form.cleaned_data.get('phone_number')
            u.save()
            return HttpResponseRedirect('/homepage/index')
        else:
            print('you done messed up')
    template_vars = {
        'form': form,
    }
    return dmp_render_to_response(request, 'editaccount.html', template_vars)

class edit_form(forms.Form):
    username = forms.CharField(label='username', required=True, max_length=300)
    first_name = forms.CharField(label='first_name', required=True, max_length=300)
    last_name = forms.CharField(label='last_name', required=True, max_length=300)
    email = forms.EmailField(label='email', required=True)
    address1 = forms.CharField(label='address1', required=True, max_length=300)
    address2 = forms.CharField(label='address2', required=True, max_length=300)
    birth = forms.DateField(label='birth', required=True)
    phone_number = forms.CharField(label='phone_number', required=True, max_length=20)

    def clean_username (self):
        if amod.User.objects.filter(username=self.cleaned_data.get('username')).exclude(id=self.userid).count() > 0:
            raise forms.ValidationError('That username already exists in our system.')
        return self.cleaned_data['username']
