from django.db import models

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
    

    



