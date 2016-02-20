from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View
from django_mako_plus.controller import view_function
from .. import dmp_render, dmp_render_to_response
from django_mako_plus.controller.router import get_renderer
from django import forms
import  catalog.models as cmod
from bootstrap3_datetime.widgets import DateTimePicker
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required, user_passes_test
from django.forms import ModelChoiceField

@login_required
@user_passes_test(lambda u: u.has_perm('Can add venue'))
@view_function
def process_request(request):
     venues = cmod.Venue.objects.all().order_by('venueName')
     template_vars = {
         'venues': venues,
     }
     return dmp_render_to_response(request, 'venues.html', template_vars)

@login_required
@user_passes_test(lambda u: u.has_perm('Can change venue'))
@view_function
def edit(request):
    try:
        v = cmod.Venue.objects.get(id=int(request.urlparams[0]))
    except cmod.Venue.DoesNotExist as e:
        return HttpResponseRedirect('/catalog/venues')

    if request.method != "POST":
        form = edit_form( initial = {
            'venueName' : v.venueName,
            'address' : v.address,
            'city' : v.city,
            'state' : v.state,
            'zipcode' : v.zipcode,
            'phoneNumber' : v.phoneNumber,
            'contactName' : v.contactName,
        })

    if request.method == "POST":
        form = edit_form(request.POST)
        if form.is_valid():
            v.venueName = form.cleaned_data.get('venueName')
            v.address = form.cleaned_data.get('address')
            v.city = form.cleaned_data.get('city')
            v.state = form.cleaned_data.get('state')
            v.zipcode = form.cleaned_data.get('zipcode')
            v.phoneNumber = form.cleaned_data.get('phoneNumber')
            v.contactName = form.cleaned_data.get('contactName')
            v.save()
            return HttpResponse('''
            <script>
                window.location.reload();
            </script>
            ''')

    areas = cmod.Area.objects.filter(venue_id=int(request.urlparams[0]))
    template_vars = {
        'areas': areas,
        'form': form,
        'venueid' : v.id,
    }
    return dmp_render_to_response(request, 'editvenue.html', template_vars)


class edit_form(forms.Form):
    venueName = forms.CharField(label='Venue Name:', required=True, max_length=30,widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Venue Name'}))
    address = forms.CharField(label='Address:', required=True, max_length=30,widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Address'}))
    city = forms.CharField(label='City:', required=True, max_length=30,widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'City'}))
    state = forms.CharField(label='State:', required=True, max_length=30,widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'State'}))
    zipcode = forms.CharField(label='Zip Code:', required=True, max_length=30,widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Zip Code'}))
    phoneNumber = forms.CharField(label='Phone Number:', required=True, max_length=30,widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Phone Number'}))
    contactName = forms.CharField(label='Contact Name:', required=True, max_length=30,widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Contact Name'}))

@login_required
@user_passes_test(lambda u: u.has_perm('Can delete venue'))
@view_function
def delete(request):
    v = cmod.Venue.objects.get(id=int(request.urlparams[0]))
    v.delete()
    return HttpResponseRedirect('/catalog/venues')

@login_required
@user_passes_test(lambda u: u.has_perm('Can add venue'))
@view_function
def create (request):
    form = createvenue_form()
    if request.method == "POST":
        form = createvenue_form(request.POST)
        if form.is_valid():
            v = cmod.Venue()
            v.venueName = form.cleaned_data.get('venueName')
            v.address = form.cleaned_data.get('address')
            v.city = form.cleaned_data.get('city')
            v.state = form.cleaned_data.get('state')
            v.zipcode = form.cleaned_data.get('zipcode')
            v.phoneNumber = form.cleaned_data.get('phoneNumber')
            v.contactName = form.cleaned_data.get('contactName')
            v.save()
            return HttpResponse('''
            <script>
                window.location.reload();
            </script>
            ''')
    template_vars = {
        'form': form,
    }
    return dmp_render_to_response(request, 'createvenue.html', template_vars)

class createvenue_form(forms.Form):
    venueName = forms.CharField(label='Venue Name:', required=True, max_length=30,widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Venue Name'}))
    address = forms.CharField(label='Address:', required=True, max_length=30,widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Address'}))
    city = forms.CharField(label='City:', required=True, max_length=30,widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'City'}))
    state = forms.CharField(label='State:', required=True, max_length=30,widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'State'}))
    zipcode = forms.CharField(label='Zip Code:', required=True, max_length=30,widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Zip Code'}))
    phoneNumber = forms.CharField(label='Phone Number:', required=True, max_length=30,widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Phone Number'}))
    contactName = forms.CharField(label='Contact Name:', required=True, max_length=30,widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Contact Name'}))

###############################
##########AREA#################
###############################
@login_required
@user_passes_test(lambda u: u.has_perm('Can add area'))
@view_function
def createarea (request):
    form = createarea_form()
    if request.method == "POST":
        form = createarea_form(request.POST)
        if form.is_valid():
            a = cmod.Area()
            a.areaName = form.cleaned_data.get('areaName')
            a.location = form.cleaned_data.get('location')
            a.description = form.cleaned_data.get('description')
            venue = cmod.Venue.objects.get(id = int(request.urlparams[0]))
            a.venue = venue
            a.save()
            return HttpResponse('''
            <script>
                window.location.reload();
            </script>
            ''')
    template_vars = {
        'form': form,
        'venueid' : request.urlparams[0]
    }
    return dmp_render_to_response(request, 'createarea.html', template_vars)

class createarea_form(forms.Form):
    areaName = forms.CharField(label='Area Name:', required=True, max_length=30,widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Area Name'}))
    location = forms.CharField(label='Location:', required=True, max_length=30,widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Location'}))
    description = forms.CharField(label='Description:', required=True, max_length=30,widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Description'}))

@login_required
@user_passes_test(lambda u: u.has_perm('Can delete area'))
@view_function
def deletearea(request):
    a = cmod.Area.objects.get(id=int(request.urlparams[0]))
    a.delete()
    return HttpResponseRedirect('/catalog/venues')

@login_required
@user_passes_test(lambda u: u.has_perm('Can change area'))
@view_function
def editarea (request):
    try:
        a = cmod.Area.objects.get(id=int(request.urlparams[0]))
    except cmod.Area.DoesNotExist as e:
        return HttpResponseRedirect('/catalog/venues')

    if request.method != "POST":
        form = editarea_form( initial = {
            'areaName' : a.areaName,
            'location' : a.location,
            'description' : a.description,
            'venue' : a.venue.venueName,
        })

    if request.method == "POST":
        form = editarea_form(request.POST)
        if form.is_valid():
            a.areaName = form.cleaned_data.get('areaName')
            a.location = form.cleaned_data.get('location')
            a.description = form.cleaned_data.get('description')
            #venue = cmod.Venue.objects.get(id = int(request.urlparams[0]))
            #a.venue = venue
            a.save()
            return HttpResponseRedirect('/catalog/venues')
    template_vars = {
        'form': form,
        'areaid' : request.urlparams[0]
    }
    return dmp_render_to_response(request, 'editarea.html', template_vars)

class editarea_form(forms.Form):
    areaName = forms.CharField(label='Area Name:', required=True, max_length=30,widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Area Name'}))
    location = forms.CharField(label='Location:', required=True, max_length=30,widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Location'}))
    description = forms.CharField(label='Description:', required=True, max_length=30,widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Description'}))
