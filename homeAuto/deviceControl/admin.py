from django.contrib import admin
from django.db.models.functions import Lower
# Register your models here.
from .models import Device, DeviceType, Location, Room




class DeviceAdmin(admin.ModelAdmin):
    #fields = ["display_name", "ip", "type", "room"]
    list_display = ["display_name", "room",  "ip", "type"]
    search_fields = ["display_name"]

    def get_ordering(self, request):
        return [Lower('room')]  # sort case insensitive

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