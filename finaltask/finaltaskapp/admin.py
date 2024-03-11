from django.contrib import admin
from .models import department,course,order
# Register your models here.
admin.site.register(department)
admin.site.register(course)
admin.site.register(order)