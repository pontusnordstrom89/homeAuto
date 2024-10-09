from django.db import models

class Device(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    display_name = models.CharField(max_length=200)
    ip = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    room = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True, blank=True)
    state = models.BooleanField(default=False)

    def __str__(self):

        return self.display_name

