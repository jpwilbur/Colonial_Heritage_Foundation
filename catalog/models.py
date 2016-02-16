from django.db import models
from Account import models as accountModels
from django.contrib import admin
from polymorphic.models import PolymorphicModel
#############################
#######   PRODUCTS    #######
#############################

class Product(PolymorphicModel):
    """docstring for Product"""
    productID = models.TextField()
    name = models.TextField()
    description = models.TextField()
    replacementValue = models.TextField()
    photoFileName = models.TextField(null = True, blank = True)
    size = models.TextField(null = True, blank = True)
    weight = models.DecimalField(max_digits=6, decimal_places=2,null = True, blank = True)

admin.site.register(Product)

class IndividualProduct(Product):
    """This is a custom product that you make"""
    creationDate = models.DateTimeField()
    customizationNotes = models.TextField()
#    Creator = models.ForeignKey(Creator)    uncomment this when we have the creator class made

admin.site.register(IndividualProduct)

class BulkProduct(Product):
    """This is a product that you would buy in bulk"""
    currentBulkPrice = models.DecimalField(max_digits=6, decimal_places=2)
    quantityAvailable = models.IntegerField()

admin.site.register(BulkProduct)

class RentalProduct(Product):
    """This is a product that you would rent out"""
    currentRentalRate = models.DecimalField(max_digits=6, decimal_places=2)
    available = models.BooleanField()

admin.site.register(RentalProduct)

######################################
#######   EVENT, VENUE, AREA   #######
######################################

class Venue(PolymorphicModel):
    venueName = models.TextField()
    address = models.TextField()
    city = models.TextField()
    state = models.TextField()
    codezip = models.TextField()
    phoneNumber = models.TextField()
    contactName = models.TextField()

admin.site.register(Venue)

class Event(PolymorphicModel):
    eventName = models.TextField()
    startDate = models.DateTimeField()
    endDate = models.DateTimeField()
    venue = models.ForeignKey(Venue, null = True, blank = True)

admin.site.register(Event)

class Area(PolymorphicModel):
    areaName = models.TextField()
    location = models.TextField()
    description = models.TextField()
    venue = models.ForeignKey(Venue)
    members = models.ManyToManyField(
        accountModels.User,
        through = 'Assignment',
    )

admin.site.register(Area)

class Assignment(PolymorphicModel):
    user = models.ForeignKey(accountModels.User, on_delete = models.CASCADE)
    area = models.ForeignKey(Area, on_delete = models.CASCADE)
    jobTitle = models.TextField()
    description = models.TextField()

admin.site.register(Assignment)
