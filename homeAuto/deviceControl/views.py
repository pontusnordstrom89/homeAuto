from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import loader
from django.http import JsonResponse
from django.conf import settings
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

    first_launch = settings.FIRST_LAUNCH
    print("Is it first launch?")
    print(first_launch)
    if first_launch == True:
        subscribe()
        print(first_launch)
        settings.FIRST_LAUNCH = False

    

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

def leave_home(request):
    # Turn off all devices
    all_active_devices = Device.objects.filter(state=True)

    for device in all_active_devices:
        print(device.display_name)
        mqtt_client.publish(f'cmnd/{device.name}/POWER', 'OFF')

    print("LEAVING HOME!!")
    
    return redirect('deviceindex', room_name = "control")