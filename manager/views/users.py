from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View
from django_mako_plus.controller import view_function
from .. import dmp_render, dmp_render_to_response
from django_mako_plus.controller.router import get_renderer
from django import forms
import  Account.models as amod
from bootstrap3_datetime.widgets import DateTimePicker

@view_function
def process_request(request):
     users = amod.User.objects.all().order_by('last_name','first_name')

     template_vars = {
         'users': users,
     }
     return dmp_render_to_response(request, 'users.html', template_vars)

@view_function
def edit(request):

    try:
        u = amod.User.objects.get(id=int(request.urlparams[0]))
    except amod.User.DoesNotExist as e:
        return HttpResponseRedirect('/manager/users')

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
        form.userid = u.id
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
            return HttpResponse('''
            <script>
                window.location.reload();
            </script>
            ''')

    users = amod.User.objects.all().order_by('last_name','first_name')
    form.userid = u.id
    template_vars = {
        'users': users,
        'form': form,
        'first_name' : u.first_name,
        'last_name' : u.last_name,
        'userid' : u.id
    }
    return dmp_render_to_response(request, 'edituser.html', template_vars)

class edit_form(forms.Form):
    username = forms.CharField(label='Username:', required=True, max_length=30,widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Username'}))
    password = forms.CharField(label='Password:', required=True, max_length=20,widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Password'}))
    first_name = forms.CharField(label='First Name:', required=True, max_length=30,widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'First Name'}))
    last_name = forms.CharField(label='Last Name:', required=True, max_length=30,widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Last Name'}))
    email = forms.EmailField(label='Email:', required=True,widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Email'}))
    address1 = forms.CharField(label='Address 1:', required=True, max_length=30,widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Address 1'}))
    address2 = forms.CharField(label='Address 2:', required=False, max_length=30,widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Address 2'}))
    birth = forms.DateField(label='Birth Date:', required=True,widget=DateTimePicker(attrs={'placeholder': 'YYYY-MM-DD'},options={"format": "YYYY-MM-DD","pickTime": False}))
    phone_number = forms.CharField(label='Phone Number:', required=True, max_length=20,widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Phone Number'}))

    def clean_username (self):
        if amod.User.objects.filter(username=self.cleaned_data.get('username')).exclude(id=self.userid).count() > 0:
            raise forms.ValidationError('That username already exists in our system.')
        return self.cleaned_data['username']

@view_function
def delete(request):
    # if request.user.is_authenticated():
    #     return HttpResponseRedirect('/manager/users')
    u = amod.User.objects.get(id=int(request.urlparams[0]))
    u.delete()
    return HttpResponseRedirect('/manager/users')


@view_function
def create (request):
    form = createuser_form()
    if request.method == "POST":
        form = createuser_form(request.POST)
        if form.is_valid():
            u = amod.User()
            u.username = form.cleaned_data.get('username')
            u.set_password(form.cleaned_data.get('password'))
            u.first_name = form.cleaned_data.get('first_name')
            u.last_name = form.cleaned_data.get('last_name')
            u.email = form.cleaned_data.get('email')
            u.address1 = form.cleaned_data.get('address1')
            u.address2 = form.cleaned_data.get('address2')
            u.birth = form.cleaned_data.get('birth')
            u.phone_number = form.cleaned_data.get('phone_number')
            u.save()
            return HttpResponse('''
            <script>
                window.location.reload();
            </script>
            ''')
    template_vars = {
        'form': form,
    }
    return dmp_render_to_response(request, 'createuser.html', template_vars)


class createuser_form(forms.Form):
    username = forms.CharField(label='Username:', required=True, max_length=30,widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Username'}))
    password = forms.CharField(label='Password:', required=True, max_length=20,widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Password'}))
    first_name = forms.CharField(label='First Name:', required=True, max_length=30,widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'First Name'}))
    last_name = forms.CharField(label='Last Name:', required=True, max_length=30,widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Last Name'}))
    email = forms.EmailField(label='Email:', required=True,widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Email'}))
    address1 = forms.CharField(label='Address 1:', required=True, max_length=30,widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Address 1'}))
    address2 = forms.CharField(label='Address 2:', required=False, max_length=30,widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Address 2'}))
    birth = forms.DateField(label='Birth Date:', required=True,widget=DateTimePicker(attrs={'placeholder': 'YYYY-MM-DD'},options={"format": "YYYY-MM-DD","pickTime": False}))
    phone_number = forms.CharField(label='Phone Number:', required=True, max_length=20,widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Phone Number'}))

    def clean_username (self):
        if amod.User.objects.filter(username=self.cleaned_data.get('username')).count() > 0:
            raise forms.ValidationError('That username already exists in our system.')
        return self.cleaned_data['username']
