from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View
from django_mako_plus.controller import view_function
from .. import dmp_render, dmp_render_to_response
from django_mako_plus.controller.router import get_renderer
from django import forms
import catalog.models as cmod
from bootstrap3_datetime.widgets import DateTimePicker
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required, user_passes_test

# @login_required
# @user_passes_test(lambda u: u.has_perm('Can add product'), login_url='/homepage/index/')
@view_function
def process_request(request):
     indproducts = cmod.IndividualProduct.objects.all().order_by('name')
     rentproducts = cmod.RentalProduct.objects.all().order_by('name')
     bulkproducts = cmod.BulkProduct.objects.all().order_by('name')
     template_vars = {
         'indproducts': indproducts,
         'rentproducts': rentproducts,
         'bulkproducts': bulkproducts,
     }
     return dmp_render_to_response(request, 'products.html', template_vars)

@view_function
def edit(request):

    try:
        p = cmod.Product.objects.get(id=int(request.urlparams[0]))
    except cmod.Product.DoesNotExist as e:
        return HttpResponseRedirect('/catalog/products')

    if request.urlparams[1] == 'indproduct':
        form = edit_form( initial = {
            'name' : p.name,
            'description' : p.description,
            'replacementValue' : p.replacementValue,
            'photoFileName' : p.photoFileName,
            'size' : p.size,
            'weight' : p.weight,
            'creationDate' : p.creationDate,
            'customizationNotes' : p.customizationNotes,
        })
        ptype = 'indproduct'
    elif request.urlparams[1] == 'bulkproduct':
        form = edit_form( initial = {
            'name' : p.name,
            'description' : p.description,
            'replacementValue' : p.replacementValue,
            'photoFileName' : p.photoFileName,
            'size' : p.size,
            'weight' : p.weight,
            'currentBulkPrice' : p.currentBulkPrice,
            'quantityAvailable' : p.quantityAvailable,
        })
        ptype = 'bulkproduct'
    elif request.urlparams[1] == 'rentalproduct':
        form = edit_form( initial = {
            'name' : p.name,
            'description' : p.description,
            'replacementValue' : p.replacementValue,
            'photoFileName' : p.photoFileName,
            'size' : p.size,
            'weight' : p.weight,
            'currentRentalRate' : p.currentRentalRate,
            'available' : p.available,
        })
        ptype = 'rentalproduct'

    if request.method == "POST":
        form = edit_form(request.POST)
        if form.is_valid():
            if form.cleaned_data.get('productType') == 'indproduct':
                p = cmod.IndividualProduct()
                p.creationDate = form.cleaned_data.get('creationDate')
                p.customizationNotes = form.cleaned_data.get('customizationNotes')
            elif form.cleaned_data.get('productType') == 'bulkproduct':
                p = cmod.BulkProduct()
                p.currentBulkPrice = form.cleaned_data.get('currentBulkPrice')
                p.quantityAvailable = form.cleaned_data.get('quantityAvailable')
            elif form.cleaned_data.get('productType') == 'rentalproduct':
                p = cmod.RentalProduct()
                p.currentRentalRate = form.cleaned_data.get('currentRentalRate')
                p.available = form.cleaned_data.get('available')
            p.name = form.cleaned_data.get('name')
            p.description = form.cleaned_data.get('description')
            p.replacementValue = form.cleaned_data.get('replacementValue')
            p.photoFileName = form.cleaned_data.get('photoFileName')
            p.size = form.cleaned_data.get('size')
            p.weight = form.cleaned_data.get('weight')
            p.save()
            return HttpResponse('''
            <script>
                window.location.reload();
            </script>
            ''')

    products = cmod.Product.objects.all().order_by('last_name','first_name')
    template_vars = {
        'form': form,
        'productid' : p.id,
        'ptype' : ptype,
    }
    return dmp_render_to_response(request, 'editproduct.html', template_vars)

class edit_form(forms.Form):
    name = forms.CharField(label='Product Name:', required=True, max_length=30,widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Product Name'}))
    #productType = forms.ChoiceField(label='Group:', required=True,choices=PRODUCT_TYPE,widget=forms.Select(attrs={'class':'form-control'}))
    description = forms.CharField(label='Description:', required=True, max_length=30,widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Description'}))
    replacementValue = forms.CharField(label='Replacement Value:', required=True, max_length=30,widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Replacement Value'}))
    photoFileName = forms.CharField(label='Photo File:', required=True, max_length=30,widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Photo File'}))
    size = forms.CharField(label='Size:', required=True, max_length=30,widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Size'}))
    weight = forms.CharField(label='Weight:', required=True, max_length=30,widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Weight'}))
    creationDate = forms.CharField(label='Creation Date:', required=False, max_length=30,widget=forms.TextInput(attrs={'id':'creationDate','class':'form-control','placeholder': 'Creation Date'}))
    customizationNotes = forms.CharField(label='Customization Notes:', required=False, max_length=30,widget=forms.TextInput(attrs={'id':'customizationNotes','class':'form-control','placeholder': 'Customization Notes'}))
    currentBulkPrice = forms.CharField(label='Current Bulk Price:', required=False, max_length=30,widget=forms.TextInput(attrs={'id':'currentBulkPrice','class':'form-control','placeholder': 'Current Bulk Price'}))
    quantityAvailable = forms.CharField(label='Quantity Available:', required=False, max_length=30,widget=forms.TextInput(attrs={'id':'quantityAvailable','class':'form-control','placeholder': 'Quantity Available'}))
    currentRentalRate = forms.CharField(label='Current Rental Price:', required=False, max_length=30,widget=forms.TextInput(attrs={'id':'currentRentalRate','class':'form-control','placeholder': 'Current Rental Price'}))
    available = forms.CharField(label='Available?:', required=False, max_length=30,widget=forms.TextInput(attrs={'id':'available','class':'form-control','placeholder': 'Available'}))


    def clean_username (self):
        if cmod.User.objects.filter(username=self.cleaned_data.get('username')).exclude(id=self.userid).count() > 0:
            raise forms.ValidationError('That username already exists in our system.')
        return self.cleaned_data['username']

#function to change user password
@view_function
def changepassword(request):

    #find user if they exist; used for changing password if POST
    u = cmod.User.objects.get(id=int(request.urlparams[0]))
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
    #     return HttpResponseRedirect('/catalog/products')
    u = cmod.Product.objects.get(id=int(request.urlparams[0]))
    u.delete()
    return HttpResponseRedirect('/catalog/products')


@view_function
def create (request):
    form = createproduct_form()
    if request.method == "POST":
        form = createproduct_form(request.POST)
        if form.is_valid():
            if form.cleaned_data.get('productType') == 'indproduct':
                p = cmod.IndividualProduct()
                p.creationDate = form.cleaned_data.get('creationDate')
                p.customizationNotes = form.cleaned_data.get('customizationNotes')
            elif form.cleaned_data.get('productType') == 'bulkproduct':
                p = cmod.BulkProduct()
                p.currentBulkPrice = form.cleaned_data.get('currentBulkPrice')
                p.quantityAvailable = form.cleaned_data.get('quantityAvailable')
            elif form.cleaned_data.get('productType') == 'rentalprdoduct':
                p = cmod.RentalProduct()
                p.currentRentalRate = form.cleaned_data.get('currentRentalRate')
                p.available = form.cleaned_data.get('available')
            p.name = form.cleaned_data.get('name')
            p.description = form.cleaned_data.get('description')
            p.replacementValue = form.cleaned_data.get('replacementValue')
            p.photoFileName = form.cleaned_data.get('photoFileName')
            p.size = form.cleaned_data.get('size')
            p.weight = form.cleaned_data.get('weight')
            p.save()
            return HttpResponse('''
            <script>
                window.location.reload();
            </script>
            ''')
    template_vars = {
        'form': form,
    }
    return dmp_render_to_response(request, 'createproduct.html', template_vars)

PRODUCT_TYPE = (
    ('', 'Choose a Product Type'),
    ('indproduct','Individual Product'),
    ('bulkproduct', 'Bulk Product'),
    ('rentalproduct', 'Rental Product'),
)
class createproduct_form(forms.Form):
    name = forms.CharField(label='Product Name:', required=True, max_length=30,widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Product Name'}))
    productType = forms.ChoiceField(label='Group:', required=True,choices=PRODUCT_TYPE,widget=forms.Select(attrs={'class':'form-control'}))
    description = forms.CharField(label='Description:', required=True, max_length=30,widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Description'}))
    replacementValue = forms.CharField(label='Replacement Value:', required=True, max_length=30,widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Replacement Value'}))
    photoFileName = forms.CharField(label='Photo File:', required=True, max_length=30,widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Photo File'}))
    size = forms.CharField(label='Size:', required=True, max_length=30,widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Size'}))
    weight = forms.CharField(label='Weight:', required=True, max_length=30,widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Weight'}))
    creationDate = forms.CharField(label='Creation Date:', required=False, max_length=30,widget=forms.TextInput(attrs={'id':'creationDate','class':'form-control','placeholder': 'Creation Date'}))
    customizationNotes = forms.CharField(label='Customization Notes:', required=False, max_length=30,widget=forms.TextInput(attrs={'id':'customizationNotes','class':'form-control','placeholder': 'Customization Notes'}))
    currentBulkPrice = forms.CharField(label='Current Bulk Price:', required=False, max_length=30,widget=forms.TextInput(attrs={'id':'currentBulkPrice','class':'form-control','placeholder': 'Current Bulk Price'}))
    quantityAvailable = forms.CharField(label='Quantity Available:', required=False, max_length=30,widget=forms.TextInput(attrs={'id':'quantityAvailable','class':'form-control','placeholder': 'Quantity Available'}))
    currentRentalRate = forms.CharField(label='Current Rental Price:', required=False, max_length=30,widget=forms.TextInput(attrs={'id':'currentRentalRate','class':'form-control','placeholder': 'Current Rental Price'}))
    available = forms.CharField(label='Available?:', required=False, max_length=30,widget=forms.TextInput(attrs={'id':'available','class':'form-control','placeholder': 'Available'}))


    def clean_username (self):
        if cmod.Product.objects.filter(username=self.cleaned_data.get('username')).count() > 0:
            raise forms.ValidationError('That username already exists in our system.')
        return self.cleaned_data['username']
