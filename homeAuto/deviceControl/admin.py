from django.contrib import admin

# Register your models here.
from .models import Device, DeviceType, Location, Room



class DeviceAdmin(admin.ModelAdmin):
    #fields = ["display_name", "ip", "type", "room"]
    list_display = ["room", "display_name", "ip", "type"]
    search_fields = ["display_name"]

class DeviceTypeAdmin(admin.ModelAdmin):
    #fields = ["display_name", "ip", "type", "room"]
    list_display = ["id", "display_name"]
    search_fields = ["display_name"]

class LocationAdmin(admin.ModelAdmin):
    #fields = ["display_name", "ip", "type", "room"]
    list_display = ["id", "display_name", "city"]
    search_fields = ["display_name"]

class RoomAdmin(admin.ModelAdmin):
    #fields = ["display_name", "ip", "type", "room"]
    list_display = ["id", "display_name"]
    search_fields = ["display_name"]


admin.site.register(Device, DeviceAdmin)
admin.site.register(DeviceType, DeviceTypeAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Room, RoomAdmin)