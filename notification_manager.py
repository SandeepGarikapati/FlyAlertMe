import os
from twilio.rest import Client
id=os.environ["TWILLIO_ID"]
key=os.environ["TWILLIO_TOKEN"]


class NotificationManager:
    def __init__(self):
        self.client=Client(id,key)

    def send_sms(self,message_body):

        message = self.client.messages.create(
            from_=os.environ["TWILLIO_PHONE_NO"],
            body=message_body,
            to=os.environ["TWILLIO_PHONE_NO"]
        )
        print(message.sid)
