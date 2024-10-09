from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import JsonResponse
from deviceControl.mqtt import client as mqtt_client
from .models import Device
from .mqtt import subscribe
import json



def publish_message(request):
    request_data = json.loads(request.body)
    rc, mid = mqtt_client.publish(request_data['topic'], request_data['msg'])
    return JsonResponse({'code': rc})

def index(request):
    # Subscribe to all topics and update status
    subscribe()

    # List all devices
    device_list = Device.objects.all()
    template = loader.get_template("deviceControl/index.html")
    context = {
        "device_list": device_list,
    }
    return HttpResponse(template.render(context, request))


def lobby(request):
    return render(request, "deviceControl/lobby.html")


def room(request, room_name):
    return render(request, "deviceControl/socketTest.html", {"room_name": room_name})
