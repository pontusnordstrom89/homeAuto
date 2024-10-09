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

def set_get_state_indicator(request):
    
    print("we're in!!!!")
    if request.method == 'GET':
        # Access the query parameters
        device = request.GET.get('device') 
        print(device)

        mqtt_client.publish(f'cmnd/{device}/POWER', 'TOGGLE')
        
        # Simulating a state (You can retrieve this from the database or any other logic)
        state = {'state': True}  # This could be 'offline', 'busy', etc.

    return JsonResponse(state)
    
    

