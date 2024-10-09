# deviceControl/consumers.py
import json

from channels.generic.websocket import WebsocketConsumer
from deviceControl.mqtt import client as mqtt_client

class ActionConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        id = text_data_json["id"]
        print(f"buttonID: {id}")

        response = {
            "id": id,
            "state": True
        }

        mqtt_client.publish(f'cmnd/{id}/POWER', 'TOGGLE')

        self.send(text_data=json.dumps(response))

    def broadcast(self, deviceStatus):
        print("trying to send")
        self.base_send = [r"ws/deviceControl/", self.as_asgi()]
        self.send(text_data=json.dumps({"message": "message"}))
    