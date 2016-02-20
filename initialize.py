# initialize the django code
print('Initializing Django...')
import sys, os
mydir = os.path.abspath(os.path.dirname(__file__))
sys.path.append(mydir)
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Colonial_Heritage_Foundation.settings")
django.setup()

# regular imports
from Account import models as amod
from catalog import models as cmod
import datetime, random, sys
from django.contrib.auth.models import Group, Permission, ContentType
#print("You should not be running this.  No soup for you.")
#sys.exit(0)

#####################################
###   Create Permissions and Groups

print()
print('Creating permissions and groups...')


######################################
###   Users

# create groups
Group.objects.all().delete()

for data in [
  ['Admin'],
  ['Manager'],
  ['Guest'],
]:
    g = Group()
    g.name = data[0]

    g.save()
    print(g)

permissions = Permission.objects.all()

for p in permissions:
  g = Group.objects.get(name='Admin')
  g.permissions.add(p)

  g.save()

for p in permissions:
  g = Group.objects.get(name='Manager')
  if p.id > 15:
    g.permissions.add(p)

  g.save()

print()
print('Creating users...')
amod.User.objects.all().delete()
users = []  # to save for use later
for i in range(1, 10):
  u = amod.User()
  u.username = 'user%i' % i
  u.first_name = 'First%i' % i
  u.last_name = 'Last%i' % i
  u.email = 'me%i@me.com' % i
  u.set_password('pass%i' % i)
  u.address = 'Address%i' % i
  u.city = 'City%i' % i
  u.state = 'State%i' % i
  u.zipcode = '%i0000' % i
  u.birth = datetime.datetime.now()
  u.phoneNumber = '555-555-000%i' % i
  u.is_active = True
  u.save()
  if i == 1:
    u.is_staff = True
    u.is_superuser = True
    g = Group.objects.get(name='Admin')
    u.groups.add(g)
  elif i == 2:
    g = Group.objects.get(name='Manager')
    u.groups.add(g)
  else:
    g = Group.objects.get(name='Guest')
    u.groups.add(g)
  u.save()
  print(u)
  print(u.groups.all())
  users.append(u)
  # assign user to some groups/permissions
print('user1, pass1 is the superuser, and the admin')
print('user2 is the manager')




#####################################
###   Products

print()
print('Creating products...')

### NO!  Products cannot be created because they don't really exist.  Never do this:
#p = cmod.Product()

# rental items
cmod.IndividualProduct.objects.all().delete()
cmod.BulkProduct.objects.all().delete()
cmod.RentalProduct.objects.all().delete()
cmod.Product.objects.all().delete()


# individual products

for i in range(1, 5):
  p = cmod.IndividualProduct()
  p.name = 'IndividualProduct%i' % i
  p.description = 'This product, #%i, is an individual product.  It is a bit of a loner.' % i
  p.replacementValue = '$%i' % i
  p.photoFileName = 'product%i.png' % i
  p.size = 'Size of product%i' % i
  p.weight = i
  p.creationDate = datetime.datetime.now()
  p.customizationNotes = 'These are product %i''s customization notes. Make it look really pretty!!' % i
  p.save()
  print(p)

# bulk products

for i in range(1, 5):
  p = cmod.BulkProduct()
  p.name = 'BulkProduct%i' % i
  p.description = 'This product, #%i, is an bulk product. It has lots of quantity.' % i
  p.replacementValue = '$%i' % i
  p.photoFileName = 'product%i.png' % i
  p.size = 'Size of the product%i' % i
  p.weight = i
  p.currentBulkPrice = i
  p.quantityAvailable = random.randint(1, 100)
  p.save()
  print(p)

# Rental Products

for i in range(1, 5):
  p = cmod.RentalProduct()
  p.name = 'RentalProduct%i' % i
  p.description = 'This product, #%i, is an rental product. It has lots of quantity.' % i
  p.replacementValue = '$%i' % i
  p.photoFileName = 'product%i.png' % i
  p.size = 'Size of the product%i' % i
  p.weight = i
  p.currentRentalRate = i
  p.available = True
  p.save()
  print(p)

# Create Dummy venues
cmod.Venue.objects.all().delete()
venues = []
for i in range(1, 5):
  v = cmod.Venue()
  v.venueName = 'Venue Name%i' % i
  v.address = 'Venue Name%i address' % i
  v.city = 'City%i' % i
  v.state = 'State%i' % i
  v.zipcode = '%i0000' % i
  v.phoneNumber = '(555) 555-000%i' % i
  v.contactName = 'The Gove%i' % i
  v.save()
  venues.append(v)
  print(v)

# create Events
cmod.Event.objects.all().delete()
for i in range (1, 5):
  e = cmod.Event()
  e.eventName = 'Event Name%i' % i
  e.startDate = datetime.datetime.now()
  e.endDate = datetime.datetime.now()
  e.venue = random.choice(venues)
  e.save()
  print(e)

# create areas
cmod.Area.objects.all().delete()
areas = []
for i in range (1, 5):
  a = cmod.Area()
  a.areaName = 'Area Name%i' % i
  a.location = 'Area location%i' % i
  a.description = 'Area description%i' % i
  a.venue = random.choice(venues)
  a.save()
  areas.append(a)
  print(a)

# create assignment
cmod.Assignment.objects.all().delete()
for i in range (1, 5):
  a = cmod.Assignment()
  a.user = random.choice(users)
  a.area = random.choice(areas)
  a.jobTitle = 'Job title%i' % i
  a.description = 'Assignment description%i' % i
  a.save()
  print(a)
