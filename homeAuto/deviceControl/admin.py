from django.contrib import admin

# Register your models here.
from .models import Device



class DeviceAdmin(admin.ModelAdmin):
    #fields = ["display_name", "ip", "type", "room"]
    list_display = ["id", "display_name", "ip", "type", "room"]
    search_fields = ["display_name"]


admin.site.register(Device, DeviceAdmin)