# -*- coding: utf-8 -*-
from twilio.rest import TwilioRestClient
 
account_sid = ""
auth_token = ""
client = TwilioRestClient(account_sid, auth_token)
 
message = client.sms.messages.create(to="", 
                                     from_="",
                                     body="You're making incredible progress!")
