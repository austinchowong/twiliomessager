# -*- coding: utf-8 -*-
from twilio.rest import TwilioRestClient
 
account_sid = "ACa378a9189ff00cd821830045b7833754"
auth_token = "dae50280b34f0b2d1c72c5ad144d498c"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.sms.messages.create(to="", 
                                     from_="",
                                     body="You're making incredible progress!")
