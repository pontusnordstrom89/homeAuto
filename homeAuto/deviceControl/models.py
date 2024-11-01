from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()  # This is recommended for compatibility with custom user models

class Location(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    display_name = models.CharField(max_length=200)
    street_name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    postal = models.CharField(max_length=200)
    lat = models.CharField(max_length=200)
    long = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.display_name
class Room(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    display_name = models.CharField(max_length=200)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.display_name
    
class DeviceType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    display_name = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.display_name
class Device(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    display_name = models.CharField(max_length=200)
    ip = models.CharField(max_length=200)
    type =  models.ForeignKey(DeviceType, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True, blank=True)
    state = models.BooleanField(default=False)

    def __str__(self):
        return self.display_name
    
class DeviceGroup(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    display_name = models.CharField(max_length=200)
    device_list =  models.ManyToManyField(Device, related_name='device_list')
    created_date = models.DateTimeField(auto_now_add=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='device_group_created_by')

    def __str__(self):
        return self.display_name
    
class DeviceScenario(models.Model):

    ACTIVATE = 'activate'
    DEACTIVATE = 'deactivate'

    ACTION_CHOICES = [
        (ACTIVATE, 'Activate'),
        (DEACTIVATE, 'Deactivate'),
    ]

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    display_name = models.CharField(max_length=200)
    action = models.CharField(
        max_length=10,
        choices=ACTION_CHOICES,
        default=ACTIVATE,
    )
    device_group =  models.ForeignKey(DeviceGroup, on_delete=models.CASCADE, related_name='device_group')
    created_date = models.DateTimeField(auto_now_add=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='device_scenario_created_by')

    def __str__(self):
        return self.display_name
    

    



