from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View
from django_mako_plus.controller import view_function
from .. import dmp_render, dmp_render_to_response
from django_mako_plus.controller.router import get_renderer
from django import forms
import  Account.models as amod
from bootstrap3_datetime.widgets import DateTimePicker
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required, user_passes_test

@login_required
@user_passes_test(lambda u: u.has_perm('Can add user'), login_url='/Account/login/')
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
        'address' : u.address,
        'city' : u.city,
        'state' : u.state,
        'zipcode' : u.zipcode,
        'birth' : u.birth,
        'phoneNumber' : u.phoneNumber,
        'ccDigits' : u.ccDigits,
        'ccExpiration' : u.ccExpiration,
        'ccCVC' : u.ccCVC,
    })

    if request.method == "POST":
        form = edit_form(request.POST)
        form.userid = u.id
        if form.is_valid():
            u.username = form.cleaned_data.get('username')
            u.first_name = form.cleaned_data.get('first_name')
            u.last_name = form.cleaned_data.get('last_name')
            u.email = form.cleaned_data.get('email')
            u.address = form.cleaned_data.get('address')
            u.city = form.cleaned_data.get('city')
            u.state = form.cleaned_data.get('state')
            u.zipcode = form.cleaned_data.get('zipcode')
            u.birth = form.cleaned_data.get('birth')
            u.phoneNumber = form.cleaned_data.get('phoneNumber')
            u.ccDigits = form.cleaned_data.get('ccDigits')
            u.ccExpiration = form.cleaned_data.get('ccExpiration')
            u.ccCVC = form.cleaned_data.get('ccCVC')
            u.save()
            g = Group.objects.get(name=form.cleaned_data.get('group'))
            u.groups.add(g)
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
        'userid' : u.id,
    }
    return dmp_render_to_response(request, 'edituser.html', template_vars)

class edit_form(forms.Form):
    username = forms.CharField(label='Username:', required=True, max_length=30,widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Username'}))
    first_name = forms.CharField(label='First Name:', required=True, max_length=30,widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'First Name'}))
    last_name = forms.CharField(label='Last Name:', required=True, max_length=30,widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Last Name'}))
    email = forms.EmailField(label='Email:', required=True,widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Email'}))
    address = forms.CharField(label='Address:', required=True, max_length=30,widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Address'}))
    city = forms.CharField(label='City:', required=True, max_length=30,widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'City'}))
    state = forms.CharField(label='State:', required=True, max_length=30,widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'State'}))
    zipcode = forms.CharField(label='Zipcode:', required=True, max_length=30,widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Zipcode'}))
    birth = forms.DateField(label='Birth Date:', required=True,input_formats=['%Y-%m-%d'],widget=DateTimePicker(attrs={'placeholder': 'YYYY-MM-DD'},options={"format": "YYYY-MM-DD","pickTime": False}))
    phoneNumber = forms.CharField(label='Phone Number:', required=True, max_length=20,widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Phone Number'}))
    ccDigits = forms.CharField(label='Last four Credit Card Digits:', required=False, max_length=30,widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Credit Card Digits'}))
    ccExpiration = forms.CharField(label='Credit Card Expiration:', required=False, max_length=30,widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Credit Card Expiration'}))
    ccCVC = forms.CharField(label='Credit Card CVC:', required=False, max_length=30,widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Credit Card CVC'}))
    group = forms.ModelChoiceField(label='Group:', required=True,queryset=Group.objects.all(),widget=forms.Select(attrs={'class':'form-control'}))

    def clean_username (self):
        if amod.User.objects.filter(username=self.cleaned_data.get('username')).exclude(id=self.userid).count() > 0:
            raise forms.ValidationError('That username already exists in our system.')
        return self.cleaned_data['username']

#function to change user password
@view_function
def changepassword(request):

    #find user if they exist; used for changing password if POST
    u = amod.User.objects.get(id=int(request.urlparams[0]))
    form = changepassword_form()

    #if they hit submit button, this is true, otherwise goes over this and returns back to page with the empty form
    if request.method == "POST":
        form = changepassword_form(request.POST)
        if form.is_valid():
            u.set_password(form.cleaned_data.get('new_password1'))
            u.save()
            return HttpResponse('''
            <script>
                window.location.reload();
            </script>
            ''')
    template_vars = {
        'form': form,
        'userid' : u.id,
    }
    return dmp_render_to_response(request, 'changepassword.html', template_vars)

class changepassword_form(forms.Form):
    new_password1 = forms.CharField(label='New Password', required=True, max_length=20)
    new_password2 = forms.CharField(label='Comfirm New Password', required=True, max_length=20)

    def clean(self):
        if self.cleaned_data.get('new_password1') != self.cleaned_data.get('new_password2'):
            raise forms.ValidationError('Passwords do not match. Try again.')
        return self.cleaned_data

#function to delete user from the system
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
            u.address = form.cleaned_data.get('address')
            u.city = form.cleaned_data.get('city')
            u.state = form.cleaned_data.get('state')
            u.zipcode = form.cleaned_data.get('zipcode')
            u.birth = form.cleaned_data.get('birth')
            u.phoneNumber = form.cleaned_data.get('phoneNumber')
            u.ccDigits = form.cleaned_data.get('ccDigits')
            u.ccExpiration = form.cleaned_data.get('ccExpiration')
            u.ccCVC = form.cleaned_data.get('ccCVC')
            u.save()
            g = Group.objects.get(name=form.cleaned_data.get('group'))
            u.groups.add(g)
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
    address = forms.CharField(label='Address:', required=True, max_length=30,widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Address 1'}))
    city = forms.CharField(label='City:', required=True, max_length=30,widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'City'}))
    state = forms.CharField(label='State:', required=True, max_length=30,widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'State'}))
    zipcode = forms.CharField(label='Zipcode:', required=True, max_length=30,widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Zipcode'}))
    birth = forms.DateField(label='Birth Date:', required=True,input_formats=['%Y-%m-%d'],widget=DateTimePicker(attrs={'placeholder': 'YYYY-MM-DD'},options={"format": "YYYY-MM-DD","pickTime": False}))
    phoneNumber = forms.CharField(label='Phone Number:', required=True, max_length=20,widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Phone Number'}))
    ccDigits = forms.CharField(label='Last four Credit Card Digits:', required=False, max_length=30,widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Last four Credit Card Digits'}))
    ccExpiration = forms.CharField(label='Credit Card Expiration:', required=False, max_length=30,widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Credit Card Expiration'}))
    ccCVC = forms.CharField(label='Credit Card CVC:', required=False, max_length=30,widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Credit Card CVC'}))
    group = forms.ModelChoiceField(label='Group:', required=True,queryset=Group.objects.all(),widget=forms.Select(attrs={'class':'form-control'}))

    def clean_username (self):
        if amod.User.objects.filter(username=self.cleaned_data.get('username')).count() > 0:
            raise forms.ValidationError('That username already exists in our system.')
        return self.cleaned_data['username']
