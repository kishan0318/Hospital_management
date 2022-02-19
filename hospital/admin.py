from django.contrib import admin
from hospital.models import Appointment, Department,Contact,Beds


# Register your models here.
admin.site.register(Department)
admin.site.register(Contact)
admin.site.register(Appointment)
admin.site.register(Beds)

