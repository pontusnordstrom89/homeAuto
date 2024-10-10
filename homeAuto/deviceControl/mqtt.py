import paho.mqtt.client as mqtt
from django.conf import settings
import json


def subscribe():
        from .models import Device

        #Get all devices
        list_of_devices = Device.objects.all()

        # For every device
        for device in list_of_devices:
            # Subscribe to client messages
            print(f'Subscribing to: stat/{device.name}/RESULT')
            client.subscribe(f'stat/{device.name}/RESULT')
        
def on_connect(mqtt_client, userdata, flags, rc):
    if rc == 0:
        print('Connected successfully')
    else:
        print('Bad connection. Code:', rc)


def on_message(mqtt_client, userdata, msg):
    print(f'Received message on topic: {msg.topic} with payload: {msg.payload}')
    payload_dict = json.loads(msg.payload.decode('utf-8'))

    if payload_dict["POWER"] == "ON":
         device_status = True
    else:
         device_status = False
        
    topic_breakdown = msg.topic.split("/")
    print(topic_breakdown[1])

   
    data = {
         "type": 'toggle',
         "state": device_status,
         "id": topic_breakdown[1]
    }
    print("Before sending")

    from .consumers import StateConsumer
    cc = StateConsumer()
    cc.send_message(data)
    # Toggle devicestatus front end
    from .models import Device
    Device.objects.filter(name=topic_breakdown[1]).update(state = device_status)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set(settings.MQTT_USER, settings.MQTT_PASSWORD)
client.connect(
    host=settings.MQTT_SERVER,
    port=settings.MQTT_PORT,
    keepalive=settings.MQTT_KEEPALIVE
)