from django.contrib import admin
from .models import Report_item,UserNotification ,ContactHelp

# Register your models here.
admin.site.register(Report_item)
admin.site.register(UserNotification)
admin.site.register(ContactHelp)
