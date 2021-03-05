import json
from .models import users
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from channels.generic.websocket import WebsocketConsumer

temp_self = None

class WSConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

        global temp_self

        temp_self = self

        temp_self.send(json.dumps({'message': users.get_all_objects(users)}))


@receiver(post_save, sender=users)
@receiver(post_delete, sender=users)
def get_model_objects(sender, **kwargs):
    print(users.get_all_objects(users))

    temp_self.send(json.dumps({'message': users.get_all_objects(users)}))
