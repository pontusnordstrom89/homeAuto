from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import JsonResponse
from deviceControl.mqtt import client as mqtt_client
from .models import Device, Room
from .mqtt import subscribe
import json



def publish_message(request):
    request_data = json.loads(request.body)
    rc, mid = mqtt_client.publish(request_data['topic'], request_data['msg'])
    return JsonResponse({'code': rc})

def index(request, room_name):
    # Subscribe to all topics and update status
    subscribe()

    # List all devices
    device_list = Device.objects.all()
    room = Room.objects.all()
    template = loader.get_template("deviceControl/deviceControl.html")
    context = {
        "rooms": room,
        "device_list": device_list,
        "room_name": room_name
    }
    return HttpResponse(template.render(context, request))
