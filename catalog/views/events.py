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
@user_passes_test(lambda u: u.has_perm('Can add event'))
@view_function
def process_request(request):
     events = cmod.Event.objects.all().order_by('eventName')
     template_vars = {
         'events': events,
     }
     return dmp_render_to_response(request, 'events.html', template_vars)

@login_required
@user_passes_test(lambda u: u.has_perm('Can change event'))
@view_function
def edit(request):

    try:
        e = cmod.Event.objects.get(id=int(request.urlparams[0]))
    except cmod.Event.DoesNotExist as e:
        return HttpResponseRedirect('/catalog/events')

    if request.method != "POST":
        form = edit_form( initial = {
            'eventName' : e.eventName,
            'startDate' : e.startDate,
            'endDate' : e.endDate,
        })

    if request.method == "POST":
        form = edit_form(request.POST)
        if form.is_valid():
            e.eventName = form.cleaned_data.get('eventName')
            e.startDate = form.cleaned_data.get('startDate')
            e.endDate = form.cleaned_data.get('endDate')
            e.venue = form.cleaned_data.get('venue')
            e.save()
            return HttpResponse('''
            <script>
                window.location.reload();
            </script>
            ''')

    events = cmod.Event.objects.all().order_by('last_name','first_name')
    template_vars = {
        'events': events,
        'form': form,
        'eventid' : e.id,
    }
    return dmp_render_to_response(request, 'editevent.html', template_vars)

# VENUES = {}
# for venue in cmod.Venue.objects.all():
#     VENUES[venue] = venue.venueName

class VenueModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return "%s" % obj.venueName

class edit_form(forms.Form):
    eventName = forms.CharField(label='Event Name:', required=True, max_length=30,widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Event Name'}))
    startDate = forms.DateField(label='Start Date:', required=True,input_formats=['%Y-%m-%d'],widget=DateTimePicker(attrs={'placeholder': 'YYYY-MM-DD'},options={"format": "YYYY-MM-DD","pickTime": False}))
    endDate = forms.DateField(label='End Date:', required=True,input_formats=['%Y-%m-%d'],widget=DateTimePicker(attrs={'placeholder': 'YYYY-MM-DD'},options={"format": "YYYY-MM-DD","pickTime": False}))
    venue = VenueModelChoiceField(label='Venue:', required=True, queryset=cmod.Venue.objects.all(),to_field_name="id",widget=forms.Select(attrs={'class':'form-control'}))

@login_required
@user_passes_test(lambda u: u.has_perm('Can delete event'))
@view_function
def delete(request):
    e = cmod.Event.objects.get(id=int(request.urlparams[0]))
    e.delete()
    return HttpResponseRedirect('/catalog/events')

@login_required
@user_passes_test(lambda u: u.has_perm('Can add event'))
@view_function
def create (request):
    form = createevent_form()
    if request.method == "POST":
        form = createevent_form(request.POST)
        if form.is_valid():
            e = cmod.Event()
            e.eventName = form.cleaned_data.get('eventName')
            e.startDate = form.cleaned_data.get('startDate')
            e.endDate = form.cleaned_data.get('endDate')
            e.venue = form.cleaned_data.get('venue')
            e.save()
            return HttpResponse('''
            <script>
                window.location.reload();
            </script>
            ''')
    template_vars = {
        'form': form,
    }
    return dmp_render_to_response(request, 'createevent.html', template_vars)

class createevent_form(forms.Form):
    eventName = forms.CharField(label='Event Name:', required=True, max_length=30,widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Event Name'}))
    startDate = forms.DateField(label='Start Date:', required=True,input_formats=['%Y-%m-%d'],widget=DateTimePicker(attrs={'placeholder': 'YYYY-MM-DD'},options={"format": "YYYY-MM-DD","pickTime": False}))
    endDate = forms.DateField(label='End Date:', required=True,input_formats=['%Y-%m-%d'],widget=DateTimePicker(attrs={'placeholder': 'YYYY-MM-DD'},options={"format": "YYYY-MM-DD","pickTime": False}))
    venue = VenueModelChoiceField(label='Venue:', required=True, queryset=cmod.Venue.objects.all(),to_field_name="id",widget=forms.Select(attrs={'class':'form-control'}))
