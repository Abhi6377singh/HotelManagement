from django.contrib import admin
#from customer.models import customer
from customer.models import *

# Register your models here.
#admin.site.register(customer)

admin.site.register(customers_h)

admin.site.register(booking)

admin.site.register(Room)

admin.site.register(BookingDate)